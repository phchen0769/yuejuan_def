# Generated by Django 4.2.6 on 2023-11-13 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='papersquestions',
            name='paper',
        ),
        migrations.RemoveField(
            model_name='papersquestions',
            name='question',
        ),
        migrations.RemoveField(
            model_name='papersquestions',
            name='student',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='students',
        ),
        migrations.RemoveField(
            model_name='students',
            name='paper',
        ),
        migrations.DeleteModel(
            name='Papers',
        ),
        migrations.DeleteModel(
            name='PapersQuestions',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.AddField(
            model_name='paper',
            name='questions',
            field=models.ManyToManyField(through='papers.Answer', to='papers.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papers.paper'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papers.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papers.student'),
        ),
    ]
