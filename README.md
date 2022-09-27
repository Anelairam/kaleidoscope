#Kaleidoscope
---

## Introduction
* * Website Link goes here * *

Kaleidoscope is my fifth and last project submision for the Full Stack E-Commerece Diploma by Code Institute.

The project's theme is a photographer's website, where the photographer as the owner of it can show his work, sale his photos and offer online photography courses as well as organised photography tours. Any user has the ability to stay as simple visitor but also to register or login in order to buy any of the photographer's services. The main technologies that the application uses are: 
 - Html
 - Css
 - Bootstrap
 - Javascript
 - Python
 - Django

---

<details><summary>Contents</summary>
<p>

* [User Experience](#User-Experience)
  * [Strategy Plane](#Strategy-Plane)
  * [Scope Plane](#Scope-Plane)
    * [User Storie](#User-Stories)
  * [Skeleton Plane](#Skeleton-Plane)
  * [Wireframes](#Wireframes)
    * [Full Screen](#Full-Screen)
    * [Mobile](#mobile)
  * [Design](#design)
    * [Images](#images)
    * [Colours](#colours)
* [Database View](#database-view)
* [Data Models](#data-models)
* [Technologies Used](#technologies-used)
* [Testing](#testing-validation)
* [Deployment](#deployment)
* [Acknowledgements](#acknowledgements)

</p>
</details>

## User Experience
---

### Strategy Plane
---
Kaleidoscope is a photographer's online presense which provides the to the customer a great variety of photographs, tutorials and events. The customer can look around and take inspiration of the photographer's work, have a look to the available tutorials and check any new events that the photographer organises. 
The website is clean and aims to reach a vast target audience. Its simple design makes the navigation intuitive and easy, all the materials nicely presented to clean background, giving the business a higher chance that the customer will feel comfortable and stay on the website to navigate further.

### Scoop Plane
---
The website main goal is to make the Visiting User interested into purchasing photos, tutorials and joining photography events. The Users have to be able to register easily and manage their account immediately. The website must be responsive for all devices and easy to navigate for everyone.

#### User Stories
---

### Skeleton Plane
---
The website features a Homepage with a main navbar to navigate the main sections of the website: Home, Portfolio, Eshop, Account.

* In the Homepage there are general information regarding the photographer and his work.
* The Portfolio page displays all the pictures that the phtographer wants to show to his potential customers and followers his work regardless if they are for sale or not.
* The Portfolio page has a dedicated navigation/filtering bar where the visitor can filter the photos according to preference.
* The Eshop consists of three subpages the Photos, Tutorials and Events
   * In the Photos page, the customers can see all the photos that are for sale, the element that differenciate them from the portfolio is the price factor.
     * The Photos page has a dedicated navigation/filtering bar where the visitor can filter the photos according to preference.
   * In the Tutorials page, the customers can see all the available tutorials for sale.
   * In the Events page, the customers can see the upcoming events and joing them.
* Each photo and tutorial has its own page with a more detailed description and purchase option.
* The User will be able to Register or Login to the website anytime, thanks to the Account icon always displayed on the page header.

### Wireframes
---
The wireframes are created with Balsamiq
 
<img width="895" alt="home" src="https://user-images.githubusercontent.com/25570623/192452273-aeb9ba99-e27e-4d91-9d8d-b19f9f1b30eb.png">
<img width="895" alt="portfolio" src="https://user-images.githubusercontent.com/25570623/192452420-239a0552-42e4-4c0c-ab15-03156a855c46.png">
<img width="895" alt="product" src="https://user-images.githubusercontent.com/25570623/192452496-5be38507-b345-4f44-8a67-9d156191c817.png">
<img width="895" alt="shoppingcart" src="https://user-images.githubusercontent.com/25570623/192452501-877b448a-29fc-46fa-ad29-21746f64ff3b.png">
<img width="895" alt="εσηοπ" src="https://user-images.githubusercontent.com/25570623/192452504-4c79374b-671a-4e9c-90a7-37f60b628f8c.png">
![image](https://user-images.githubusercontent.com/25570623/192453704-dc878f23-4383-4dd4-96db-78c283b97598.png)
![image](https://user-images.githubusercontent.com/25570623/192453786-f1454ba4-d9f2-4a4a-acfc-bc5c75ab646b.png)



### Design

---

#### Images
---
* All images that are in use for the website are from [Pexels](#https://pexels.com/) .

#### Colours
---
After a lot of color testing with the final product and some research to colour constrasting and design, I chose these to colours to be mq main palete for the colour scheme of the website.These two colours give a minimal and elegant touch to the website and serve the purpose of it great, as the main focus should be the vubrant colours of the photographers work.
![image](https://user-images.githubusercontent.com/25570623/192451303-50519d0d-eaa7-4bb7-a8b1-367b3bd8e845.png)


### Database View
---
In the development of Kaleidoscope, I have used SQLite3 database as part of Django framework and Heroku PostGres to handle the database for the production version of the website.

All photos, tutorials and events have been manually created by myself. Django’s authentication system and Django Allauth are also integrated sets of Django and helped manage authentication, registration and account management. The schema below has been created with dbdiagram.io:

![image](https://user-images.githubusercontent.com/25570623/192444226-4f30c318-3a49-4ea5-9373-b641b2cf27c8.png)

### Data Models
---
Category Model

| Field  | Field Type | Field Options |
| ------------- | ------------- |------------- |
| name  | CharField  | max_length=10  |

Type Model

| Field  | Field Type | Field Options |
| ------------- | ------------- |------------- |
| name  | CharField  | max_length=25  |

Product Model

| Field  | Field Type | Field Options |
| ------------- | ------------- |------------- |
| name  | CharField  | max_length=25  |
| category  | ForeignKey  | 'Category', null=True, blank=True, on_delete=models.SET_NULL  |
| type  | ForeignKey  | 'Type', null=True, on_delete=models.SET_NULL  |
| location  | CharField  | max_length=25, null=True, blank=True  |
| size  | CharField  | max_length=200, null=True, blank=True  |
| price  | CharField  | max_digits=6, decimal_places=2, null=True, blank=True  |
| description  | CharField  | max_length=200, null=True, blank=True  |
| image  | ImageField  | null=True, blank=True  |

Difficulty Model

| Field  | Field Type | Field Options |
| ------------- | ------------- |------------- |
| name  | CharField  | max_length=20  |

Event Model

| Field  | Field Type | Field Options |
| ------------- | ------------- |------------- |
| title  | CharField  | max_length=25  |
| category  | ForeignKey  | 'Category', null=True, blank=True, on_delete=models.SET_NULL  |
| day  | DateField  |   |
| type  | ForeignKey  | 'Type', null=True, on_delete=models.SET_NULL  |
| difficulty  | ForeignKey | 'Difficulty', null=True, on_delete=models.SET_NULL  |
| startin_at  | TimeField  |   |
| ending_at  | TimeField  |   |
| description  | CharField  | max_length=500  |

Tutorial Model

| Field  | Field Type | Field Options |
| ------------- | ------------- |------------- |
| name  | CharField  | max_length=25  |
| category  | ForeignKey  | 'Category', null=True, blank=True, on_delete=models.SET_NULL  |
| type  | ForeignKey  | 'Type', null=True, on_delete=models.SET_NULL  |
| difficulty  | ForeignKey | 'Difficulty', null=True, on_delete=models.SET_NULL  |
| file  | FileField  | null=True, validators=[FileExtensionValidator( ['mp4'] ) ]  |
| price  | DecimalField  |  max_digits=6, decimal_places=2, null=True, blank=True |
| description  | CharField  | max_length=200, null=True, blank=True  |

Order Model

| Field  | Field Type | Field Options |
| ------------- | ------------- |------------- |
| order_number  | CharField  | max_length=32, null=False, editable=False  |
| full_name  | CharField  | max_length=50, null=False, blank=False  |
| email  | EmailField  | max_length=254, null=False, blank=FalseL  |
| phone_number  | CharField | max_length=20, null=False, blank=False  |
| country  | CountryField  | blank_label='Country', null=False, blank=False |
| postcode  | CharField  |  max_length=20, null=True, blank=True |
| town_or_city  | CharField  | max_length=40, null=False, blank=False  |
| street_address1  | CharField  |  max_length=80, null=False, blank=False |
| street_address2  | CharField  | max_length=80, null=True, blank=True  |
| county  | CharField  |  max_length=80, null=True, blank=True |
| date  | DateTimeField  | auto_now_add=True  |
| order_total  | DecimalField  |  max_digits=10, decimal_places=2, null=False, default=0 |
| grand_total  | DecimalField  | max_digits=10, decimal_places=2, null=False, default=0  |
| original_cart  | TextField  |  null=False, blank=False, default='' |
| stripe_pid  | CharField  | max_length=254, null=False, blank=False, default=''  |

OrderLineItem Model

| Field  | Field Type | Field Options |
| ------------- | ------------- |------------- |
| order  | ForeignKey  | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'  |
| product  | ForeignKey  | Product, null=False, blank=False, on_delete=models.CASCADE  |
| quantity  | IntegerField  | null=False, blank=False, default=0  |
| lineitem_total  | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |


### Technologies Used
---
* HTML
* CSS
* Python
* JavaScript
* Django and Django Allauth
* Bootstrap
* Font Awesome
* JQuery
* Google Fonts
* Stripe
* GitHub
* GitPod
* Heroku
* AWS

### Testing & Validation
---
* A full manual testing file can be found here.
* For python code validation I have been using pep8 online:
  * Lines left too long just when breaking them would have compromised the code integrity.
* For HTML validation I have used validatorW3
* For CSS validation I have used jigsaw.W3
* For responsiveness testing I have used Google DevTools

### Deployment
---
Kaleidoscope has been created on Gitpod, with commits pushed directly to the GitHub repository. The project has been deployed to Heroku, which was synchronized to GitHub to update the live site. The static files are stored in Amazon AWS and the payment infrastructure is managed by Stripe's software and APIs.

### Acknowledgements
---
* Code Institute for project guidance, project walkthrough and coding & learning materials.
* My mentor for support and encouragement throught the course.
* [Font Awesome](#https://fontawesome.com/) for the icon libraries.
* [Pexels](#https://pexels.com/) for the photos.
* Slack community
* Tutor Support


Thank you!
