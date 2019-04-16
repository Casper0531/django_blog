# Define Entities of Web application
# It will translated automatically Django into database tables

from django.db import models
from django.contrib.auth.models import User


# Define Tables
# Each field is represented by instances of django.db.models.Field subclasses, database columns
# CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(30) NOT NULL UNIQUE, "description" varchar(100) NOT NULL);
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#CREATE TABLE "boards_topic" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "subject" varchar(255) NOT NULL, "last_updated" datetime NOT NULL, "board_id" integer NOT NULL REFERENCES "boards_board" ("id") DEFERRABLE INITIALLY DEFERRED, "starter_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
class Topic(models.Model):
    subject = models.CharField(max_length=255)
    # auto_now_add will set the columns value to current date and time when object is created
    last_updated = models.DateTimeField(auto_now_add=True)
    # ForeignKey : Estabilish Relation between tables
    board = models.ForeignKey(Board, models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, models.CASCADE, related_name='topics')


# CREATE TABLE "boards_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "message" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NULL, "created_by_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, models.CASCADE,related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, models.CASCADE, null=True, related_name='+')


