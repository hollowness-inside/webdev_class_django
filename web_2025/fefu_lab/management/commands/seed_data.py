from django.core.management.base import BaseCommand
from fefu_lab.models import Member, Volturian, Course, Enrollment
from datetime import date


class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными'

    def handle(self, *args, **options):
        self.stdout.write('Создание тестовых данных...')

        # Очистка существующих данных
        Enrollment.objects.all().delete()
        Course.objects.all().delete()
        Member.objects.all().delete()
        Volturian.objects.all().delete()

        # Создание Вольтурианцев (покровителей)
        volturians = [
            Volturian(
                first_name='Аро',
                last_name='Вольтури',
                email='aro@volturi.it',
                ability='Чтение мыслей через прикосновение',
                degree='ANCIENT'
            ),
            Volturian(
                first_name='Маркус',
                last_name='Вольтури',
                email='marcus@volturi.it',
                ability='Видение отношений и связей',
                degree='ANCIENT'
            ),
            Volturian(
                first_name='Кай',
                last_name='Вольтури',
                email='caius@volturi.it',
                ability='Усиленная сила',
                degree='ANCIENT'
            ),
            Volturian(
                first_name='Джейн',
                last_name='Вольтури',
                email='jane@volturi.it',
                ability='Иллюзия боли',
                degree='VICTORIAN'
            ),
            Volturian(
                first_name='Алек',
                last_name='Вольтури',
                email='alec@volturi.it',
                ability='Сенсорная депривация',
                degree='VICTORIAN'
            ),
        ]

        for volturian in volturians:
            volturian.save()

        # Создание Мемберов (студентов)
        members = [
            Member(
                image='/static/web_2025/student/bella.jpg',
                first_name='Белла',
                last_name='Свон',
                email='bella.swan@forks.com',
                birth_date=date(1987, 9, 13),
                clan='CUL'
            ),
            Member(
                image='/static/web_2025/student/edward.jpg',
                first_name='Эдвард',
                last_name='Каллен',
                email='edward.cullen@forks.com',
                birth_date=date(1901, 6, 20),
                clan='CUL'
            ),
            Member(
                image='/static/web_2025/student/alice.webp',
                first_name='Элис',
                last_name='Каллен',
                email='alice.cullen@forks.com',
                birth_date=date(1901, 1, 1),
                clan='CUL'
            ),
            Member(
                image='/static/web_2025/student/jasper.jpg',
                first_name='Джаспер',
                last_name='Хейл',
                email='jasper.hale@forks.com',
                birth_date=date(1844, 1, 1),
                clan='CUL'
            ),
            Member(
                image='/static/web_2025/student/rosalie.webp',
                first_name='Розали',
                last_name='Хейл',
                email='rosalie.hale@forks.com',
                birth_date=date(1915, 1, 1),
                clan='CUL'
            ),
            Member(
                image='/static/web_2025/student/emmet.jpg',
                first_name='Эммет',
                last_name='Каллен',
                email='emmett.cullen@forks.com',
                birth_date=date(1915, 1, 1),
                clan='CUL'
            ),
            Member(
                image='/static/web_2025/student/jacob.webp',
                first_name='Джейкоб',
                last_name='Блэк',
                email='jacob.black@lapush.com',
                birth_date=date(1990, 1, 14),
                clan='QUI'
            ),
            Member(
                image='/static/web_2025/student/seth.jpg',
                first_name='Сет',
                last_name='Клируотер',
                email='seth.clearwater@lapush.com',
                birth_date=date(1992, 1, 1),
                clan='QUI'
            ),
        ]

        for member in members:
            member.save()

        # Создание Курсов
        courses = [
            Course(
                title='Основы управления жаждой',
                slug='thirst-control-basics',
                description='Базовый курс для новообращенных вампиров. Изучение техник самоконтроля, медитации и альтернативных источников питания.',
                duration=36,
                volturian=volturians[0],
                level='BEGINNER',
                max_students=25,
                price=0
            ),
            Course(
                title='Продвинутая защита разума',
                slug='advanced-mind-defense',
                description='Продвинутый курс по ментальной защите. Защита от чтения мыслей, иллюзий и других психических атак.',
                duration=48,
                volturian=volturians[0],
                level='ADVANCED',
                max_students=20,
                price=15000
            ),
            Course(
                title='Видение будущего: теория и практика',
                slug='future-vision-course',
                description='Изучение способностей предвидения. Интерпретация видений, работа с вероятностями будущего.',
                duration=42,
                volturian=volturians[1],
                level='INTERMEDIATE',
                max_students=30,
                price=12000
            ),
            Course(
                title='Боевые искусства бессмертных',
                slug='immortal-combat',
                description='Курс по вампирским боевым техникам. Использование сверхскорости, силы и регенерации в бою.',
                duration=40,
                volturian=volturians[2],
                level='ADVANCED',
                max_students=15,
                price=18000
            ),
            Course(
                title='Управление эмоциями',
                slug='emotion-manipulation',
                description='Изучение способности влиять на эмоциональное состояние окружающих. Техники успокоения и возбуждения.',
                duration=35,
                volturian=volturians[3],
                level='INTERMEDIATE',
                max_students=20,
                price=10000
            ),
            Course(
                title='История вампирских кланов',
                slug='vampire-clans-history',
                description='Всесторонний обзор истории вампирских кланов по всему миру. От древних времен до современности.',
                duration=50,
                volturian=volturians[4],
                level='BEGINNER',
                max_students=40,
                price=5000
            ),
        ]

        for course in courses:
            course.save()

        # Создание Записей на курсы
        enrollments = [
            # Белла - Управление жаждой
            Enrollment(student=members[0], course=courses[0], status='ACTIVE'),
            # Белла - Защита разума
            Enrollment(student=members[0], course=courses[1], status='ACTIVE'),
            # Эдвард - Защита разума
            Enrollment(student=members[1],
                       course=courses[1], status='COMPLETED'),
            # Эдвард - История кланов
            Enrollment(student=members[1], course=courses[5], status='ACTIVE'),
            # Элис - Видение будущего
            Enrollment(student=members[2], course=courses[2], status='ACTIVE'),
            # Элис - История кланов
            Enrollment(student=members[2], course=courses[5], status='ACTIVE'),
            # Джаспер - Управление эмоциями
            Enrollment(student=members[3], course=courses[4], status='ACTIVE'),
            # Джаспер - Боевые искусства
            Enrollment(student=members[3], course=courses[3], status='ACTIVE'),
            # Розали - Боевые искусства
            Enrollment(student=members[4], course=courses[3], status='ACTIVE'),
            # Эммет - Боевые искусства
            Enrollment(student=members[5], course=courses[3], status='ACTIVE'),
            # Эммет - Управление жаждой
            Enrollment(student=members[5],
                       course=courses[0], status='COMPLETED'),
            # Джейкоб - История кланов
            Enrollment(student=members[6], course=courses[5], status='ACTIVE'),
            # Сет - Управление жаждой
            Enrollment(student=members[7], course=courses[0], status='ACTIVE'),
        ]

        for enrollment in enrollments:
            enrollment.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Успешно создано: {len(volturians)} вольтурианцев, '
                f'{len(members)} мемберов, {len(courses)} курсов, '
                f'{len(enrollments)} записей на курсы'
            )
        )
