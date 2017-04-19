from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext
#from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
import pymongo
import json
from blog.Geolocation import geolocation
from blog.Geolocation import Distance
from PythonInsideHTML import PIH


# Create your views here.


#@login_required
def home(request):
    if request.method == 'GET':  # If the form is submitted
        a = "a"
        search_query = request.GET.get('search_box', None)
        search_zipcode =request.GET.get('zipcode', None)



        retail_store = request.GET.get('retail_store', None)
        retail_description = request.GET.get('retail_description', None)
        retail_price = request.GET.get('retail_price', None)
        retail_zipcode = request.GET.get('zipcode_retail', None)
        if search_query:
            uri = 'mongodb://instore2:123abc@ds159050.mlab.com:59050/in-store'
            client = pymongo.MongoClient(uri)
            db = client.get_default_database()
            products = db['products']

            b = []
            User_Lat = geolocation(search_zipcode)


            #a='beef'
            b = products.find({'$text': {'$search': search_query}})
    # print(type(b))
            Doc_2 = []
            Doc_2_store=[]
            Doc_2_price=[]
            Doc_2_description=[]
            for doc in b:

                doc_st= doc['store']
                doc_st1="Store: "+str(doc_st)
                doc_pr= doc['price']
                doc_pr1 = "Price: " + str(doc_pr)
                doc_des=  doc['description']
                doc_des1="Description: "+str(doc_des)
                good_loc = doc['location']
                good_loc1="Location: "+str(good_loc)
                good_ltlng = geolocation(good_loc)
                Dis_2_store = Distance(User_Lat, good_ltlng)
                Dis_2_store1= "Distance(in meters): "+str(Dis_2_store)+" m"
                doc_1 = [doc_st1, doc_pr1, doc_des1,Dis_2_store1,good_loc1]
               # doc_11=json.loads(doc_1)

                Doc_2.append(doc_1)
                Doc_2_store.append(doc_st)
                Doc_2_price.append(doc_pr)
                Doc_2_description.append(doc_des)


            #for item in Doc_2:



            len_doc2=len(Doc_2)
            Doc_2=Doc_2.sort(key=lambda x: x[3])

            Dis_2_store=Distance(User_Lat,good_ltlng)
            sorted_Doc_2= Doc_2.sort()
                #Doc_3 = str(Doc_2.append(doc_1))
            context = {
                'sorted_Doc_2':sorted_Doc_2,
                'Dis_2_store':Dis_2_store,
                'doc_pr':doc['price'],
                'good_ltlng':good_ltlng,
                'good_loc_lng': good_loc[1],
               'search_zipcode':search_zipcode,
               'User_Lat':User_Lat,
               'doc_st':doc_st,
                'Doc_2': Doc_2,
                'zip_cont':Doc_2_price,
               'len_doc2':len_doc2,
                'Doc_2_store':Doc_2_store,
                'Doc_2_price':Doc_2_price,
                'Doc_2_description':Doc_2_description,
             #'User_Lat':User_Lat
             }

            return render(request, 'blog/result.html', context)
        elif  retail_store:

            uri = 'mongodb://instore2:123abc@ds159050.mlab.com:59050/in-store'
            client = pymongo.MongoClient(uri)
            db = client.get_default_database()
            products = db['products']

            b = []

            # a='beef'
            b = products.insert({"store" : retail_store,  "price" : retail_price , 'description' : retail_description, 'location': retail_zipcode})
            return render(request,'blog/retail_info.html')
        else:
            return render(request, 'blog/home.html')





