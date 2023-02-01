from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        content_types = ContentType.objects.all()
        duplicates = []
        seen = set()
        for ct in content_types:
            print("SSSSSSSSSSs")
            key = (ct.app_label, ct.model)
            if key in seen:
                duplicates.append(key)
            else:
                seen.add(key)

        if duplicates:
            print("Duplicates found:")
            for duplicate in duplicates:
                print(f"app_label: {duplicate[0]}, model: {duplicate[1]}")
        else:
            print("No duplicates found.")