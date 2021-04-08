from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):
	help = 'rename project'

	def add_arguments(self, parser):
		parser.add_argument('new_project_name', type=str,help='the new django project name')

		#parser.add_argument('-p','--prefix')


	def handle(self, *args, **kwargs):
		new_project_name = kwargs['new_project_name']


		files_to_rename = [
							'rename_project/settings/base.py',
							'rename_project/wsgi.py',
							'rename_project/asgi.py',
							'manage.py'
							]

		folder_to_rename = 'rename_project'

		count_rename_command = 0

		if count_rename_command == 0:
			for f in files_to_rename:
				with open(f,'r') as file:
					filedata = file.read()
				filedata = filedata.replace('rename_project',new_project_name)
				
				with open(f,'w') as file:
					file.write(filedata)
			os.rename(folder_to_rename, new_project_name)		
			self.stdout.write(self.style.SUCCESS("Project has been renamed to %s \n Note:Don't try to use rename command again!!!"% new_project_name))
			count_rename_command += 1
		else:
			self.stdout.write(self.style.SUCCESS("This project already renamed !!!"))
		