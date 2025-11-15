from django.db import models
from django.urls import reverse


class Member(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Email')
    birth_date = models.DateField(
        null=True, blank=True, verbose_name='Дата рождения')
    clan = models.CharField(
        max_length=3, default='XX', verbose_name='Клан')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления')
    image = models.CharField(default="/static/web_2025/smn.png")

    class Meta:
        verbose_name = 'Мембер'
        verbose_name_plural = 'Мемберы'
        ordering = ['last_name', 'first_name']
        db_table = 'members'

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_absolute_url(self):
        return reverse('member_detail', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_faculty_display_name(self):
        return dict(self.CLAN_CHOICES).get(self.clan, 'Неизвестно')


class Volturian(models.Model):
    DEGREE_CHOICES = [
        ('NEWBORN', 'Новорождённый (начиная с 2000-х)'),
        ('VICTORIAN', 'Викторианское время (1800-х)'),
        ('VETERAN', 'Ветеран (начиная с 1500-х)'),
        ('ANCIENT', 'Древний (с рождества Христова)'),
    ]

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Email')
    ability = models.CharField(
        max_length=200, verbose_name='Способность')
    degree = models.CharField(
        max_length=20, choices=DEGREE_CHOICES, blank=True, verbose_name='Степень')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Покровитель'
        verbose_name_plural = 'Покровитель'
        ordering = ['last_name', 'first_name']
        db_table = 'volturian'

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    LEVEL_CHOICES = [
        ('BEGINNER', 'Начальный'),
        ('INTERMEDIATE', 'Средний'),
        ('ADVANCED', 'Продвинутый'),
    ]

    title = models.CharField(
        max_length=200, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Описание')
    duration = models.PositiveIntegerField(
        verbose_name='Продолжительность (часы)')
    volturian = models.ForeignKey(Volturian, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='courses', verbose_name='Вольтурианец')
    level = models.CharField(
        max_length=20, choices=LEVEL_CHOICES, default='BEGINNER', verbose_name='Уровень')
    max_students = models.PositiveIntegerField(
        default=30, verbose_name='Макс. мемберов')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name='Цена')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-created_at']
        db_table = 'courses'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Активен'),
        ('COMPLETED', 'Завершен'),
        ('DROPPED', 'Отчислен'),
    ]

    student = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='enrollments', verbose_name='Студент')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='enrollments', verbose_name='Курс')
    enrolled_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата записи')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='ACTIVE', verbose_name='Статус')

    class Meta:
        verbose_name = 'Запись на курс'
        verbose_name_plural = 'Записи на курсы'
        ordering = ['-enrolled_at']
        db_table = 'enrollments'
        unique_together = ['student', 'course']

    def __str__(self):
        return f"{self.student} - {self.course}"
