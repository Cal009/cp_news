# CP | News

Welcome to my news blog. CP|News was created to allow users to post about their interesting stories whilst being able to have a discussion about it in comments. The News posts are usually kept more simple than regular news articles allowing the users to understand more about the content rather than a article filled with adverts or other random placeholder text used in most modern news articles.

![responsive-image](static/images/main-website.png)

## Aims of the website

### The main aim for the website:
As stated above somewhere for users to post about news articles they might have seen elsewhere and allows them to discuss them in the comments section below. Users can provide feedback to the posts by either leaving comments or simply liking or disliking the individual post. 

### Authentication
For the safety of the users, when a comment is submitted it has to be reviewed by an admin of the website. Not only this but the users are unable to comment or like without first signing in or signing up for an account.

## User Experience

### Visitors to this website are looking for:
- Somewhere to share their news posts
- The ability to comment on posts
- The ability to like or dislike posts
- The option to collaborate
- A sign in and sign out option
- Clear layout with eye catching content

## Existing features

### Home Page
![responsive-image](static/images/main-website.png)

- A clear layout is kept on the main website page with a small enough pagination of 6 posts per page. This allows for users to clearly see all the content on the page without having to continuously scroll. Next to each News article is an image related to the post itself that was chosen by the author of the article. If they do not wish to choose an image themselves then one will be inserted as a placeholder. This allows the site to maintain the same design allowing for a better user experience.
- A clear nav bar is in place at the top of the screen showing the Title of the Website, "Home", "About", and depending on if youre signed in or not it will either show the "Sign out" button or the "Sign up" and "Sign in" buttons. These buttons are hidden if the user is already signed in allowing for better user Experience. Alongside this there is a comment in the top left of the main page stating "You are logged in as (User)." This gives further reiteration that the user is logged in as the correct user.

### Post detail
![responsive-image](static/images/post-detail-1.png)
![responsive-image](static/images/post-detail-2.png)

- As can be seen in the post detail section of the website the user image and title is brought across and displayed differently to the main page. It keeps the main details of the User, the image, the title and the time and date it was created. Below that you then have the main extract of the article written by authorised users.
- Below this the like and dislike button are located. Both Like and Dislike buttons work in tandem, so users can not like and also dislike as the code checks for a user input already and if its there it wil remove it or replace it depending on what the user wants to do. Next to that is the counter which clearly indicates how many likes or dislikes the post has. All the likes and dislikes are independant to each post this was achieved using the primary key.
- Next is the comment section. Same again the counter keeps track of how many comments a post has but will only count them once they have been approved. The field on the right allows for users to type their comment and submit it for review. Upon submitting as seen in the image it will be put up for review by an admin and once it is approved it will appear as a functional comment that users can edit or delete if they are the commenter.
- Finally the Footer, which is present across all webpages, which features multiple social media links and a copyright mark.

### About Page

- The about page consists of a profile image of the creator of the website alongside a text box that tells the user a bit about the site and why it was created.
- Beneath that is the collaborate section. This is where users can fill out the form to then have the admin of the site review the applications and potentially work for the site. The form has to be filled out entirely or it will not send.