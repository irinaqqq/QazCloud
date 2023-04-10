import boto3
from django.conf import settings
from django.views.generic.edit import FormView
from .forms import UploadForm
from .models import Post


class UploadView(FormView):
    template_name = 'index.html'
    form_class = UploadForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        file_url = form.instance.file.url
        bucket_name = 'qazcloud1'

        # Get the list of files in the S3 bucket
        s3 = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
        bucket = s3.Bucket(bucket_name)
        files = bucket.objects.all()

        # Filter the list to include only files with the specified prefix
        prefix = 'media/'
        files = [file for file in files if file.key.startswith(prefix)]

        # Create a list of Post objects from the files
        posts = [Post(file=file.key[len(prefix):]) for file in files]

        context = self.get_context_data(file_url=file_url, posts=posts)
        return self.render_to_response(context)
