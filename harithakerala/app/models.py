from django.db import models

# Create your models here.


class district(models.Model):
    district_id=models.CharField(max_length=50, primary_key=True)
    district_name = models.CharField(max_length=50, null=True)
   
    
    
    class Meta:
        db_table = "district"


class login(models.Model):
    username=models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=50, null=True)
    category=models.CharField(max_length=50, null=True)
    

    
   
    
    
    class Meta:
        db_table = "login"           


class fee(models.Model):
    fee_id=models.CharField(max_length=50, primary_key=True)
    fee_name = models.CharField(max_length=50, null=True)
    fee_description = models.CharField(max_length=50, null=True)
    fee_amount = models.IntegerField(max_length=50, null=True)
    fee_date = models.CharField(max_length=50, null=True)
   
    
    
    class Meta:
        db_table = "fee"        


class localbody(models.Model):
    local_id=models.CharField(max_length=50, primary_key=True)
    district_id = models.ForeignKey(district, on_delete= models.CASCADE)
    # local_district=models.CharField(max_length=50, null=True)
    local_name = models.CharField(max_length=50, null=True)
    local_category = models.CharField(max_length=50, null=True)
    
   
    
    
    class Meta:
        db_table = "localbody"   



class ward(models.Model):
    ward_id=models.CharField(max_length=50, primary_key=True)
    local_id=models.ForeignKey(localbody, on_delete= models.CASCADE)
    ward_number = models.CharField(max_length=50, null=True)
    ward_membername = models.CharField(max_length=50, null=True)
    ward_contact = models.IntegerField(max_length=50, null=True)
    ward_email = models.CharField(max_length=50, null=True)
   
    
    
    class Meta:
        db_table = "ward"     


class house(models.Model):
    house_number=models.CharField(max_length=50, primary_key=True)
    ward_id=models.ForeignKey(ward, on_delete= models.CASCADE)
    house_name = models.CharField(max_length=50, null=True)
    house_ownername = models.CharField(max_length=50, null=True)
    house_location = models.CharField(max_length=50, null=True)
    house_address = models.CharField(max_length=50, null=True) 
    house_aadhar = models.CharField(max_length=50, null=True)
    house_contact = models.CharField(max_length=50, null=True)

   
    
    
    class Meta:
        db_table = "house"  

class house3(models.Model):
    house_number=models.CharField(max_length=50, primary_key=True)
    ward_id=models.ForeignKey(ward, on_delete= models.CASCADE)
    house_name = models.CharField(max_length=50, null=True)
    house_ownername = models.CharField(max_length=50, null=True)
    house_location = models.CharField(max_length=50, null=True)
    house_address = models.CharField(max_length=50, null=True) 
    house_aadhar = models.CharField(max_length=50, null=True)
    house_contact = models.CharField(max_length=50, null=True)
    house_email = models.CharField(max_length=50, null=True)

   
    
    
    class Meta:
        db_table = "house3"           



class duty(models.Model):
    duty_id=models.CharField(max_length=50, primary_key=True)
    duty_name = models.CharField(max_length=50, null=True)
    duty_description = models.CharField(max_length=50, null=True)
   
    
    
    class Meta:
        db_table = "duty"  


class harithakaramasena(models.Model):
    hks_id=models.CharField(max_length=50, primary_key=True) 
    hks_name = models.CharField(max_length=50, null=True)
    hks_address = models.CharField(max_length=50, null=True)
    hks_gender = models.CharField(max_length=50, null=True)
    hks_age = models.CharField(max_length=50, null=True)
    hks_phonenumber = models.CharField(max_length=50, null=True) 
    hks_email = models.CharField(max_length=50, null=True)
    ward_id=models.ForeignKey(ward, on_delete= models.CASCADE)
    hks_date = models.CharField(max_length=50, null=True)
    hks_photo = models.CharField(max_length=50, null=True)

   
    
    
    class Meta:
        db_table = "harithakaramasena"  


class complaint(models.Model):
    complaint_id=models.CharField(max_length=50, primary_key=True)
    house_number=models.ForeignKey(house3, on_delete= models.CASCADE)
    complaint_complaint= models.CharField(max_length=50, null=True)
    
    
    
    class Meta:
        db_table = "complaint"   


class applications(models.Model):
    request_id=models.CharField(max_length=50, primary_key=True) 
    request_name = models.CharField(max_length=50, null=True)
    request_address = models.CharField(max_length=50, null=True)
    request_dob = models.CharField(max_length=50, null=True)
    request_gender = models.CharField(max_length=50, null=True)
    request_age = models.CharField(max_length=50, null=True)
    request_qualification = models.CharField(max_length=50, null=True)
    district_id=models.ForeignKey(district, on_delete= models.CASCADE)
    ward_id=models.ForeignKey(ward, on_delete= models.CASCADE)
    local_id=models.ForeignKey(localbody, on_delete= models.CASCADE)
    request_rationcardtype = models.CharField(max_length=50, null=True)
    request_income = models.IntegerField()
    request_phonenumber = models.CharField(max_length=50, null=True)
    request_email = models.CharField(max_length=50, null=True)
    request_photo = models.CharField(max_length=50, null=True)
    request_inomecertificate = models.CharField(max_length=50, null=True)
    request_aadhardcard = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)

   
    
    
    class Meta:
        db_table = "applications"   



     

class wardallot1(models.Model):
    allot_id=models.CharField(max_length=50, primary_key=True) 
    ward_id=models.ForeignKey(ward, on_delete= models.CASCADE)
   
    duty_id=models.ForeignKey(duty, on_delete= models.CASCADE)
    starting_date = models.CharField(max_length=50, null=True)
    ending_date = models.CharField(max_length=50, null=True)
    

   
    
    
    class Meta:
        db_table = "wardallot1"                                 




class houseallot(models.Model):
    allothouse_id=models.CharField(max_length=50, primary_key=True) 
    hks_id=models.ForeignKey(harithakaramasena, on_delete= models.CASCADE)
    allot_id=models.ForeignKey(wardallot1, on_delete= models.CASCADE)
   
    # starting_housenumber = models.CharField(max_length=50, null=True)
    # ending_housenumber = models.CharField(max_length=50, null=True)
    house_number=models.ForeignKey(house3, on_delete= models.CASCADE)
   

   
    
    
    class Meta:
        db_table = "houseallot"   


class complainthks(models.Model):
    complainthks_id=models.CharField(max_length=50, primary_key=True)
    hks_id=models.ForeignKey(harithakaramasena, on_delete= models.CASCADE)
    complainthks_complaint= models.CharField(max_length=50, null=True)
    
    
    
    class Meta:
        db_table = "complainthks"   


class housecollectiondetails(models.Model):
    collection_id=models.CharField(max_length=50, primary_key=True)
    ward_id=models.ForeignKey(ward, on_delete= models.CASCADE)
    house_number= models.ForeignKey(house3, on_delete= models.CASCADE)
    duty_id= models.ForeignKey(duty, on_delete= models.CASCADE)
    collection_month= models.CharField(max_length=50, null=True)
    collection_year= models.CharField(max_length=50, null=True)
    collection_date= models.CharField(max_length=50, null=True)
    collection_fee= models.CharField(max_length=50, null=True)
  
    
    
    
    class Meta:
        db_table = "housecollectiondetails"    


class function(models.Model):
    function_id=models.CharField(max_length=50, primary_key=True)
    house_number= models.ForeignKey(house3, on_delete= models.CASCADE)
    ward_id=models.ForeignKey(ward, on_delete= models.CASCADE)
    function_date= models.CharField(max_length=50, null=True)
    function_type= models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    
    
    
    class Meta:
        db_table = "function"  

class foodbalance(models.Model):
    foodbalance_id=models.CharField(max_length=50, primary_key=True)
    function_id=models.ForeignKey(function, on_delete= models.CASCADE)
    food_type= models.CharField(max_length=50, null=True)
    food_quantity= models.CharField(max_length=50, null=True)
    food_preparationtime= models.CharField(max_length=50, null=True)
    food_usebefore= models.CharField(max_length=50, null=True)
    food_collectionpoint= models.CharField(max_length=50, null=True)
    
    
    
    class Meta:
        db_table = "foodbalance"                             


class requestfood(models.Model):
    foodrequest_id=models.CharField(max_length=50, primary_key=True)
    foodbalance_id_id=models.ForeignKey(foodbalance, on_delete= models.CASCADE)
    house_number= models.ForeignKey(house3, on_delete= models.CASCADE)
    request_time= models.CharField(max_length=50, null=True)
    request_date= models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    
    
    
    class Meta:
        db_table = "requestfood" 


class payment(models.Model):
    payment_id=models.CharField(max_length=50, primary_key=True)
    hks_id=models.ForeignKey(harithakaramasena, on_delete= models.CASCADE)
    house_number= models.ForeignKey(house3, on_delete= models.CASCADE)
    # duty_id= models.ForeignKey(duty, on_delete= models.CASCADE)
    payment_month= models.CharField(max_length=50, null=True)
    
    payment_date= models.CharField(max_length=50, null=True)
    payment_amount= models.CharField(max_length=50, null=True)
    payment_sack= models.CharField(max_length=50, null=True)
    payment_finalamount= models.CharField(max_length=50, null=True)
  
    
    
    
    class Meta:
        db_table = "payment"          

class idgen(models.Model):
    did = models.IntegerField()
    fee_id = models.IntegerField()
    local_id = models.IntegerField()
    ward_id = models.IntegerField()
    duty_id = models.IntegerField()
    hks_id =  models.IntegerField()
    cmp_id =  models.IntegerField()
    request_id =  models.IntegerField()
    allot_id =  models.IntegerField()
    allothouse_id =  models.IntegerField()
    cmphks_id =  models.IntegerField()
    collection_id =  models.IntegerField()
    function_id =  models.IntegerField()
    foodbalance_id =  models.IntegerField()
    foodrequest_id =  models.IntegerField()
    payment_id =  models.IntegerField()


    class Meta:
        db_table ="idgen"           


