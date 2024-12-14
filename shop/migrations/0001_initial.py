# Generated by Django 5.1.4 on 2024-12-13 13:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('name', models.CharField(max_length=200)),
            ],
            bases=('shop.basemodel',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, default='image/category.png', null=True, upload_to='image')),
                ('description', models.TextField()),
            ],
            bases=('shop.basemodel',),
        ),
        migrations.CreateModel(
            name='LightBodyColour',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('bodycolour', models.CharField(max_length=200)),
            ],
            bases=('shop.basemodel',),
        ),
        migrations.CreateModel(
            name='LightColour',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('colour', models.CharField(max_length=200)),
            ],
            bases=('shop.basemodel',),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('light_material', models.CharField(max_length=200)),
            ],
            bases=('shop.basemodel',),
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('name', models.CharField(max_length=200)),
            ],
            bases=('shop.basemodel',),
        ),
        migrations.CreateModel(
            name='Wates',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('light_wates', models.CharField(max_length=200)),
            ],
            bases=('shop.basemodel',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('bio', models.CharField(max_length=200, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='profile_picture/default.png', null=True, upload_to='profile_picture')),
                ('phone', models.CharField(max_length=200, null=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('shop.basemodel',),
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('preview_image', models.ImageField(blank=True, default='preview_image/image.png', null=True, upload_to='previewimage')),
                ('price', models.PositiveIntegerField()),
                ('brand_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.brand')),
                ('category_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('distributer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('body_object', models.ManyToManyField(to='shop.lightbodycolour')),
                ('colour_object', models.ManyToManyField(to='shop.lightcolour')),
                ('material_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.material')),
                ('shape_object', models.ManyToManyField(to='shop.shape')),
                ('wates_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.wates')),
            ],
            bases=('shop.basemodel',),
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('shop.basemodel',),
        ),
        migrations.CreateModel(
            name='WishListItem',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('is_order_placed', models.BooleanField(default=False)),
                ('body_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.lightbodycolour')),
                ('colour_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.lightcolour')),
                ('light_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.light')),
                ('shape_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shape')),
                ('wishlist_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_item', to='shop.wishlist')),
            ],
            bases=('shop.basemodel',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.basemodel')),
                ('delivery_address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=100)),
                ('payment_mode', models.CharField(choices=[('online', 'online'), ('cod', 'cod')], default='cod', max_length=100)),
                ('order_id', models.CharField(max_length=200, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('order_confirmed', 'Order confirmed'), ('dispatched', 'Dispatched'), ('in_transit', 'In transit'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='order_confirmed', max_length=200)),
                ('user_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myorders', to=settings.AUTH_USER_MODEL)),
                ('wishlistitem_objects', models.ManyToManyField(to='shop.wishlistitem')),
            ],
            bases=('shop.basemodel',),
        ),
    ]
