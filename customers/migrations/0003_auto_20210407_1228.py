# Generated by Django 3.2 on 2021-04-07 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_delete_gift'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='plan_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=100)),
                ('recipient_email', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]
