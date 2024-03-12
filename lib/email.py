import resend
from jinja2 import Environment, FileSystemLoader

from core.config import app_config

class Email:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Email, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
      resend.api_key = app_config.RESEND_API_KEY

    
    def build_template(self, template_path, template_params):
      file_loader = FileSystemLoader('templates')
      env = Environment(loader=file_loader)
      template = env.get_template(template_path)

      output = template.render(template_params)

      return output

    def send_email(self, to, subject, template_path, template_params):
      output = self.build_template(template_path, template_params)

      params = {
          "from": "Team <team@conceptcodes.dev>",
          "to": [to],
          "subject": subject,
          "html": output,
      }

      email = resend.Emails.send(params)

      return email

email_client = Email()
