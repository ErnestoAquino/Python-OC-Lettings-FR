Database Structure and Data Models
===================================

The application is composed of two main apps: Lettings and Profiles. Each contains models that represent the database structure and facilitate interaction with the stored data.

Lettings App
------------

The Lettings app is designed to manage information related to rentals. It includes the following models:

- **Address**: This model represents a physical address. It stores details such as street number, street name, city, state, postal code, and country code. Addresses are used to precisely locate real estate properties available for rent.

- **Letting**: This model represents a real estate property available for rent. It contains information such as the listing title and the property's address. Each Letting is associated with a unique Address through a one-to-one relationship, allowing each property to be linked to a specific address.

Profiles App
------------

The Profiles app is for managing user profiles. It contains the following model:

- **Profile**: This model represents a user's profile. It is linked to a User account through a one-to-one relationship and contains additional information such as the user's favorite city. The Profile model allows for extending the standard user information provided by Django with application-specific data.

Relationships Between Models
-----------------------------

- **Address and Letting**: There is a one-to-one relationship between Address and Letting, meaning that each address corresponds to a unique rental property, and vice versa. This relationship is established via a OneToOneField in the Letting model.

- **User and Profile**: Similarly, a one-to-one relationship connects the User model (provided by Django) and Profile model, allowing for the association of specific profile information with each user. This relationship is also established via a OneToOneField in the Profile model.
