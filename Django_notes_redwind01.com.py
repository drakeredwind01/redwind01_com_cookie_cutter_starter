# https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html
# docker compose -f local.yml run --rm django python manage.py createsuperuser
import random

docker compose -f local.yml run --rm django python manage.py makemigrations
docker compose -f local.yml run --rm django python manage.py migrate
docker compose -f local.yml run --rm django python manage.py createsuperuser
docker compose -f local.yml run --rm django python manage.py startapp
docker compose -f local.yml run --rm django python manage.py build          # create new image that docker uses when you run it with docker up

docker-compose -f local.yml run -p 8000:8000 --rm django /bin/bash          # make a bash terminal on linux within docker
    # can be used to explore the docker image
docker-compose -f local.yml run --rm django /bin/bash       # make a bash terminal on linux within docker
python manage.py                                            # ctrl+d to exit docker compose /bin/bash
python manage.py runserver
docker-compose -f local.yml up
# python manage.py startapp     not working

# for production
docker-compose -f production.yml build
docker-compose -f production.yml up


GIT
    git log                     # 'what happend git?'
    git status                  # 'what's happening, git?'
    git pull origin full_backup # pull from git branch 'full_backup' (if it existes)
    git add --all               # add everything to the commit
    git commit -m 'Initial commit all files to repository'   # commit with custom message
    git push                    # push your files to github
    git branch -a               # list all branches
    git checkout master         # switch to existing 'master' branch
    git checkout -b master      # create and switch to 'master' branch

    django-admin startproject {project_name}
    python .\manage.py startapp {app_name}
    python .\manage.py runserver



when committing add .txt to this file







app/settings.py
config/settings/base.py





def navigate_file_structure():
    pass # ctrl+f12 (then go to it using enter or f4)
def quick_switch_scheme():
    pass # ctrl+back_quote(`):
def View_recent_files():
    pass # ctrl+e
def surround_code_fragment():
    pass # ctrl+alt+t
def show_usages():
    pass # ctrl+alt+f7



cyberlancer models notes
"""
jobs
application
companies


"""



def changed():
    pre-commit-config.yaml
        # - id: check-json

        #  - repo: https://github.com/PyCQA/flake8
        #    rev: 6.1.0
        #    hooks:
        #      - id: flake8




git
    git reset --hard 1520a2c2b1ee27e21d630a8cfad623a6e80ea3bb


talimeir reproduction are on the ends of dna (kind of like aglets)
we need a way to repair the aglet



def adding_models():          # add admin.py

    adding models
    terminal
        python manage.py startapp {APPNAME example cyberlancer} # look this up
    config/settings/base.py
        LOCAL_APPS = [
        "cyberlancer",
        ]
    cyberlancer/models.py
        from django.db.models import CharField, PositiveSmallIntegerField
        class UserData(models.Model):
            username = models.CharField(max_length=50,default="defalut title",help_text="This is where you put your title", )
            ratings = models.PositiveSmallIntegerField(default=100,help_text="This is where you put a system for rating and reviewing the client and freelancer", )
    cyberlancer/serializer.py
        from cyberlancer.models import UserData
        class UserDataSerializer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = UserData
                fields = '__all__'
    cyberlancer/views.py
        from .models import UserData
        from .serializer import UserDataSerializer
        class UserDataViewSet(viewsets.ModelViewSet):
            queryset = UserData.objects.all()
            serializer_class = UserDataSerializer
    config/api_router.py
        from cyberlancer.views import UserDataViewSet
        router.register("users", UserDataViewSet)
    config/urls.py
        from cyberlancer.views import UserDataViewSet
        path("api/cyberlancer/UserDataViewSet",
            UserDataViewSet.as_view({"get": "list"}),
            name="User_Data_View_Set", ),
    admin.py
        from .models import UserData
        @admin.register(UserData)
        class UserDataAdmin(admin.ModelAdmin):
            list_display = [f.name for f in UserData._meta.fields]
            or
            fields = ["challengepic", "challengetitle", "challenge1number", "challenge1money", "challenge2number",
                "challenge2money", "challenge3number", "challenge3money", "challenge4number", "challenge4money",
                "challenge5number", "challenge5money", "description", "status", "user", "created_at",
                "time_to_complete", "skills", "participants", "blank", ]
    views.py
        from django.shortcuts import render
        from rest_framework import viewsets

        from .models import Skills
        from .serializers import SkillsSerializer  # Import your serializer

        # easiest for api
        class SkillsViewSet(viewsets.ModelViewSet):
            queryset = Skills.objects.all()
            serializer_class = SkillsSerializer
            # extra
            def get_context_data(self, **kwargs):
                # Call the base implementation first to get a context
                context = super().get_context_data(**kwargs)
                # Add in a QuerySet of all the books
                context["skill_data_list"] = Skills.objects.all()
                return context
    # for .html.css.java
        views.py
            from django.views.generic import TemplateView
            class CyberbaseSkillsTemplateView(TemplateView):
                template_name = "challenges.html"

        config.urls.py
            path("redwind01.com/ActiveChallengeDataViewSet/", ActiveChallengeDataTemplateView.as_view()),

        templates.books.html
            <!-- fields -->
            {% for skill in skill_data_list %}
            <ul class="nav flex-column">
                <li class="nav-item">
                    <a class="nav-link active" href="#">
                        {{ skill.skillname|lower }}
                    </a>
                </li>
                {% endfor %}




        models.py
            from django.conf import settings
            from django.db.models import DO_NOTHING, ForeignKey
            class Books(models.Model):
                checked_out_to2 = ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=DO_NOTHING)









def adding_models():          # add admin.py

    adding models
    1 terminal
        python manage.py startapp {APPNAME example library} # look this up
    2 config/settings/base.py
        LOCAL_APPS = [
        "library",
        ]
    3 library/models.py
        from django.db.models import CharField, PositiveSmallIntegerField
        class books(models.Model):
            username = models.CharField(max_length=50,default="defalut title",help_text="This is where you put your title", )
            ratings = models.PositiveSmallIntegerField(default=100,help_text="This is where you put a system for rating and reviewing the client and freelancer", )
    4 library/serializer.py
        from library.models import Books
        class BooksSerializer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Books
                fields = '__all__'
    5 library/views.py
        from .models import Books
        from .serializer import BooksSerializer
        class BooksViewSet(viewsets.ModelViewSet):
            queryset = Books.objects.all()
            serializer_class = BooksSerializer
    6 config/api_router.py
        from library.views import BooksViewSet
        router.register("users", BooksViewSet)
    7 config/urls.py
        from library.views import BooksViewSet
        path("api/library/BooksViewSet",
            BooksViewSet.as_view({"get": "list"}),
            name="User_Data_View_Set", ),
    8 library.admin.py
        from .models import Books
        @admin.register(Books)
        class BooksAdmin(admin.ModelAdmin):
            list_display = [f.name for f in Books._meta.fields]
            or
            fields = ["challengepic", "challengetitle", "challenge1number", "challenge1money", "challenge2number",
                "challenge2money", "challenge3number", "challenge3money", "challenge4number", "challenge4money",
                "challenge5number", "challenge5money", "description", "status", "user", "created_at",
                "time_to_complete", "skills", "participants", "blank", ]
    9 views.py
        from django.shortcuts import render
        from rest_framework import viewsets

        from .models import Skills
        from .serializers import SkillsSerializer  # Import your serializer

        class SkillsViewSet(viewsets.ModelViewSet):
            queryset = Skills.objects.all()
            serializer_class = SkillsSerializer
            def get_context_data(self, **kwargs):
                # Call the base implementation first to get a context
                context = super().get_context_data(**kwargs)
                # Add in a QuerySet of all the books
                context["skill_data_list"] = Skills.objects.all()
                return context
    # for .html.css.java
    from library.views import BooksTemplateView
        path("books/", BooksTemplateView.as_view()),

    10 templates.cyberbase.html
        <!-- fields -->
        {% for skill in skill_data_list %}
        <ul class="nav flex-column">
            <li class="nav-item">
                <a class="nav-link active" href="#">
                    {{ skill.skillname|lower }}
                </a>
            </li>
            {% endfor %}






# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

D:
mkdir D:\documents\GitHub\redwind01_com_cookie_cutter_starter
cd D:\documents\GitHub\redwind01_com_cookie_cutter_starter
activate redwind01env
cookiecutter gh:cookiecutter/cookiecutter-django
y
redwind01_com_cookie_cutter_starter # project_name
redwind01_com_cookie_cutter_starter # project_slug
redwind01_com_cookie_cutter_starter # description
drake redwind # author_name
redwind01.com # domain_name
drakeredwind01@gmail.com # email
0.1.0 # version
5   # 1 open_source_license MIT
1   # username_type
UTC # timezone
y   # windows
2   # Select editor
y   # use_docker
1   # postgresql_version 15
4   # cloud_provider 4 NONE
9   # mail_service Other SMTP
y   # use_async
y   # use_drf
1   # frontend_pipeline None
y   # use_celery
n   # use_mailpit
y   # use_sentry
y   # use_whitenoise
n   # use_heroku
4   # ci_tool NONE
n   # keep_local_envs_in_vcs
y   # debug





















  [1/27] project_name (My Awesome Project): redwind01_com_cookie_cutter_starter
  [2/27] project_slug (redwind01_com_cookie_cutter_starter): redwind01_com_cookie_cutter_starter
  [3/27] description (Behold My Awesome Project!): redwind01_com_cookie_cutter_starter
  [4/27] author_name (Daniel Roy Greenfeld): drake redwind
  [5/27] domain_name (example.com): redwind01.com
  [6/27] email (drake-redwind@redwind01.com): drakeredwind01@gmail.com
  [7/27] version (0.1.0):
  [8/27] Select open_source_license
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from [1/2/3/4/5] (1): 1
  [9/27] Select username_type
    1 - username
    2 - email
    Choose from [1/2] (1): 1
  [10/27] timezone (UTC): UTC
  [11/27] windows (n): y
  [12/27] Select editor
    1 - None
    2 - PyCharm
    3 - VS Code
    Choose from [1/2/3] (1): 2
  [13/27] use_docker (n): y
  [14/27] Select postgresql_version
    1 - 15
    2 - 14
    3 - 13
    4 - 12
    5 - 11
    6 - 10
    Choose from [1/2/3/4/5/6] (1): 1
  [15/27] Select cloud_provider
    1 - AWS
    2 - GCP
    3 - Azure
    4 - None
    Choose from [1/2/3/4] (1): 4
  [16/27] Select mail_service
    1 - Mailgun
    2 - Amazon SES
    3 - Mailjet
    4 - Mandrill
    5 - Postmark
    6 - Sendgrid
    7 - SendinBlue
    8 - SparkPost
    9 - Other SMTP
    Choose from [1/2/3/4/5/6/7/8/9] (1): 1
  [17/27] use_async (n): y
  [18/27] use_drf (n): y
  [19/27] Select frontend_pipeline
    1 - None
    2 - Django Compressor
    3 - Gulp
    4 - Webpack
    Choose from [1/2/3/4] (1): 1
  [20/27] use_celery (n): y
  [21/27] use_mailpit (n): n
  [22/27] use_sentry (n): y
  [23/27] use_whitenoise (n): y
  [24/27] use_heroku (n): n
  [25/27] Select ci_tool
    1 - None
    2 - Travis
    3 - Gitlab
    4 - Github
    5 - Drone
    Choose from [1/2/3/4/5] (1): 4
  [26/27] keep_local_envs_in_vcs (y): n
  [27/27] debug (n): y


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # unsure of this
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # config/urls.py
    #     from cyberlancer import views
    #     from cyberlancer.views import UserDataViewSet
    #     urlpatterns += [
    #     path(
    #         "views/home",
    #         views.CyberlancerHome.as_view(),
    #         name="cyberlancerhome",
    #     ),
    #     path(
    #         "api/cyberlancer/UserDataViewSet",
    #         UserDataViewSet.as_view({"get": "list"}),
    #         name="User_Data_View_Set",
    #     ),
    #     path(
    #         "redwind01.com/cyberlancer/templates/base.html",
    #         SellersViewSet.as_view({"get": "list"}),
    #         name="Sellers_View_Set",
    #     ),

    # def Loading_Modules_and_Third_Party_Tag_Libraries():
        # There are over seventy-five tags and filters built into Django
        # To use a tag or filter that comes with Django but isn’t in the standard set, you need to:

        # 1 Register the package's Django app
        # 2 Load the template library into your template


        # A popular package that comes with Django but isn’t part of the built-in library is humanize.
        # This library has filters that change numeric data into more readable forms.
        # Because it ships as part of the contrib module in Django, there’s no additional installation step.
        # config/settings/base.py
        #     INSTALLED_APPS = ["django.contrib.humanize",]




def create_users_programmatically():     # add admin.py
    from django.contrib.auth.models import User

    # Create user and save to the database
    user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

    # Update fields and then save again
    user.first_name = 'Tyrone'
    user.last_name = 'Citizen'
    user.save()





def Authentication():
    pass
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#template_directory
    TODO: skipped some stuff os go back and get it
    Template directory
        redwind01.com\config\settings\base.py
            make sure have      'DIRS': [os.path.join(BASE_DIR, 'templates')],
            and                 'APP_DIRS': True,


D:\documents\GitHub\redwind01_com_cookie_cutter_starter\.gitignore
#.env
#.envs/*
.envs/.production









END
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$





timeline
    models
    views
















def HELP():
    # TODO: don't understand https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#testing_in_views
        LoginRequiredMixin

def later_to_add_on():

    class UserData(models.Model):
        name = models.CharField(
            max_length=50,
            default="defalut title",
            help_text="This is where you put the experience required for the job",
        )
        datestuff = models.DateField(
            help_text="This is where you put the deadline for the job"
        )
        ratingsoverview = models.CharField(
            max_length = 5,
            default = "cpe",
            choices = deprecated_or_obsolete_choices,
            help_text = "This is where you put how you want people to contact you",
            choices = deprecated_or_obsolete_choices,
        )




def to_look_up():


2023.08.25.21.42.16.368
    ChoiceField.choices
        file:///D:/documents/GitHub/redwind01.com/redwind01/Documentation/django-readthedocs-io-en-latest/contents.html#django.forms.ChoiceField.choices


def to_send_to_devs():
    2023.08.25.21.57.50.696
        include BAD.py
        black and flake don't like each other

TODO:

TODO:
[X] get api running
[ ] .html for books         end first tut
[ ] plugin ALL.AUTH
[ ] save database export
[ ] database import
[ ] payment wallet, escrow
[ ] add model constraints
[ ] add read only settings


go through git tut for command line
