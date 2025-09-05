import csv

from django.contrib.auth.models import User
from django.http import StreamingHttpResponse
from django.views.generic import TemplateView


class Echo:
    """An object that implements just the write method of the file-like interface."""

    @staticmethod
    def write(value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


class DownloadCSVView(TemplateView):

    def get(self, request, *args, **kwargs):
        pseudo_buffer = Echo()
        writer = csv.writer(pseudo_buffer)
        content_disposition = 'attachment; filename="test.csv"'

        return StreamingHttpResponse(
            (writer.writerow(row) for row in self.iter_rows()),
            content_type="text/csv",
            headers={"Content-Disposition": content_disposition},
        )

    def iter_rows(self):
        yield ["id", "username"]
        users_qs = User.objects.all()
        for user in users_qs:
            yield [user.id, user.username]