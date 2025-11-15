from django.contrib import admin
from .models import Member, Volturian, Course, Enrollment


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'clan', 'is_active', 'created_at']
    list_filter = ['is_active', 'clan', 'created_at']
    search_fields = ['first_name', 'last_name', 'email']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Детали', {
            'fields': ('birth_date', 'clan', 'is_active')
        }),
        ('Системные поля', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Volturian)
class VolturianAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'ability', 'degree', 'is_active']
    list_filter = ['is_active', 'degree']
    search_fields = ['first_name', 'last_name', 'email', 'ability']
    readonly_fields = ['created_at']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'volturian', 'duration',
                    'level', 'max_students', 'price', 'is_active']
    list_filter = ['is_active', 'level', 'volturian']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'description')
        }),
        ('Детали курса', {
            'fields': ('volturian', 'duration', 'level', 'max_students', 'price', 'is_active')
        }),
        ('Системные поля', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'status', 'enrolled_at']
    list_filter = ['status', 'enrolled_at']
    search_fields = ['student__first_name',
                     'student__last_name', 'course__title']
    readonly_fields = ['enrolled_at']
    autocomplete_fields = ['student', 'course']
