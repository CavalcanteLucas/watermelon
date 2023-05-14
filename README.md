# Watermelon

This app is a simple form that asks the user a few questions and then shows the results.

Access it at: https://watermelon--beta.vercel.app/.

## Running the app

1. Clone the repository to your local machine.
2. Make sure Docker and docker-compose are installed on your machine.
3. Open a terminal window and navigate to the project directory.
4. Run the following command [^1]:

```
docker-compser -f docker-compose.yml up --build
```
5. Once the containers are up and running, open your web browser and go to:

```
http://localhost:8000
```

[^1]: Make sure the port 5432 is **not** in use! If it is, consider stoping your local postgresql server. In case you're in linux, you can do it by running: `sudo service postgresql stop`.

## Implementation Specs

The following specs have been implemented:
- The Seller Onboarding Form is the first thing a user sees on landing on the site.
- The Seller Onboarding Form has 6 questions.
    - Each question is displayed alone, sequentially.
- The completed forms are displayd in a page for the results.
    - No authentication is required to see the results.
- It is written in Python and Django.
- If the user hits back or forward with the form's buttons, she stays within the same Entry.
- The application is deployed in Vercel.
    - The application has also been shipped with Docker and docker-compose.

This spec has **not** been implemented within the given time limit:
- If the user hits refresh on the browser, a new Entry is created in the page of results.

## Bonus Specs

The following bonus specs have been implemented:

- Graphical improvements:
    - Centralization of the important content;
    - Colors and fonts;
    - Responsiveness.

- User experience (UX) improvements:
    - The user can see how many steps are left;
    - There is a link to the results page from the form page;
    - There is a link to the form page from the results page;
    - The button does not shift places from one question to the other.

These bonus specs have not been implemented within the given time limit:
- Question validation;
- Optional questions.

### Author

**Watermelon** is developed by **Lucas C Cavalcante**. If you have any questions or feedback about the app, please feel free to contact me at lucascpcavalcante@gmail.com.
