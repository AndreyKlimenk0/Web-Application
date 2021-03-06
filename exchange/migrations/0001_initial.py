from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('key', models.CharField(max_length=255)),
                ('secret', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('time', models.IntegerField()),
                ('type_order', models.CharField(choices=[('Cell', 'Cell'), ('By', 'By')], max_length=255)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type_trade', models.CharField(choices=[('Fill', 'Fill'), ('Part-Fill', 'Part fill'), ('Cancel', 'Cancel')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privider_id', models.IntegerField()),
                ('type_trade', models.CharField(choices=[('Fill', 'Заполнить'), ('Part-Fill', 'Неполное заполнение'), ('Cancel', 'Отменить')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('time', models.IntegerField()),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exchange.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='pair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Pair'),
        ),
        migrations.AddField(
            model_name='account',
            name='provide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Provider'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
