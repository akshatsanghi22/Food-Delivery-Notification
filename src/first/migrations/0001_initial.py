# Generated by Django 4.2.4 on 2023-08-20 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Username',
            fields=[
                ('name', models.CharField(default='Your name', max_length=20)),
                ('user_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('payment_status', models.CharField(choices=[('completed', 'Completed'), ('processing', 'Processing'), ('declined', 'Declined')], default='processing', max_length=10)),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.username')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('order_date', models.DateField(auto_now=True)),
                ('order_item', models.CharField(default='pizza', max_length=100)),
                ('restaurant_name', models.CharField(default='SST', max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.username')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notification_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('notification_text', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.orders')),
                ('payment_id', models.ForeignKey(default='DEFAULT VALUE', on_delete=django.db.models.deletion.CASCADE, to='first.payment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.username')),
            ],
        ),
    ]
