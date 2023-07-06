    # import serializers from the REST framework
    from rest_framework import serializers
     
    # import the todo data model
    from .models import Customer
     
    # create a serializer class
    class CustomerSerializer(serializers.ModelSerializer):
     
        # create a meta class
        class Meta:
            model = Customer
            fields = ('customer_id', 'customer_name')

