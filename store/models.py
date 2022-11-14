from django.db import models


class Promotion(models.Model):

    description = models.CharField(max_length=255)

    discount = models.FloatField()


class Collection(models.Model):

    title = models.CharField(max_length=255)

    #the featured class create circular relation ship becuase we are using the c;ass product 

    #before it is defined to avoid this we can treat the product as string 

    #also we use related_name='+' to tell django that the reverse relation dons't matter unless it will give us

    #error because we have already estableshed relation with the class nam Collection in product so 

    #there will be name conflict also instead of using '+' we can give it other name eg "another_name"

    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')


# we created product class that inherit from models the model class

class Product(models.Model):

    #django automatically add id class to our field but if we don'title

    #want id field id replace it with another we can set the primary key

    # to the attribute we want in this case it will be sku

    #sku = models.CharField(max_length=10, primary_key=True)

    #the title will store char field with maximum 255 length

    #and later it will create varchar(255) element in our DB

    title = models.CharField(max_length=255) 
    #slug fiels will remove space and number on the title and make it seo friendly url
    slug = models.SlugField()
    #the discription will be text field we didn't use charfield

    #because discription can be longer so in textfield

    # to set maximum length is not required so we can write longer

    #dicription with out limitation

    discription = models.TextField()

    #we use decimal field cuz float field have rounding issue

    #it is safe to use decimal field , this field have 2 requirment

    # maximum digit and decimal places after dot
    unit_price = models.DecimalField(max_digits=6 , decimal_places=2)

    #inventory attirbute will store intger

    inventory = models.IntegerField()

    #last upadate will store the last time that the product is updated

    #auto_now=true will store the last updated time but if we aslo

    #want to store when was the item created we can use "auto_now_add=true"

    last_update = models.DateTimeField(auto_now=True)

    #we will create relation with collection and on delete we will protect the product

    #because when a collection is deleted we don't want to delete the product

    #have define the class "Collection()" before this class so we could reference it

    #but if we can't arrange our code we can pass the class as string instead of as class

    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

    #since promotion is many to many relation ship it will create reverse relation automatically

    #on the promotion class for us

    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):

    #we will create list of tuples for our membership attribute which

    #have the choice option and the options will be stored here on the top

    #incase we update it later the choices will be stored in variable then we will

    #add the variable to the tuple list to make our code clean and bug free

    MEMBERSHIP_BRONZE = 'B'

    MEMBERSHIP_SILVER = 'S'

    MEMBERSHIP_GOLD = 'G'


    MEMBERSHIP_CHOICES = [

        (MEMBERSHIP_BRONZE, 'Bronze'),

        (MEMBERSHIP_SILVER, 'Silver'),

        (MEMBERSHIP_GOLD, 'GOLD')

    ]


    first_name = models.CharField(max_length=255)

    last_name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=255)

    birth_date = models.DateField(null=True)

    # choice field option will help us set choices to our db

    # eg geneder we can set 2 types of gender "male" and "female"

    #in this case we will set membership "gold" , "silver" , "bronze"

    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

  


class Order(models.Model):

    PAYMENT_STATUS_PENDING = 'P'

    PAYMENT_STATUS_COMPLETE = 'C'

    PAYMENT_STATUS_FAILED = 'F'


    PAYMENT_CHOICE = [

        (PAYMENT_STATUS_PENDING , 'Pending'),

        (PAYMENT_STATUS_COMPLETE, 'Complete'),

        (PAYMENT_STATUS_FAILED, 'Failed')

    ]


    placed_at = models.DateTimeField(auto_now_add=True)

    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICE, default=PAYMENT_STATUS_PENDING)

    #if we want to use one to one relation we can set the customer as primary key in this case

    #the customer will have only one address

    #    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

    #in this program we will use one to many relation and we will use freign key instead of onetoone

    #we will allow duplicate in this column cuz we want to allow customer to have duplicate address

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.PROTECT)

    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    #in this attribute we will only store postive integer value

    quantity = models.PositiveIntegerField()

    #we are storing the unit price again here because the base price can change at any point of time

    #so we should store the price at which the item was ordered

    unit_order = models.DecimalField(max_digits=6, decimal_places=2)



class Cart(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):

    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)

    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    quantity = models.PositiveIntegerField()



class Address(models.Model):

    street = models.CharField(max_length=255)

    city = models.CharField(max_length=255)

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
