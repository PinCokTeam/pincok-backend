from contents.models import Contents


class Menu:
    contentfields = Contents.objects.filter(Contents.title, Contents.detail)