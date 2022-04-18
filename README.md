# Inspiration Quotation

## About
* This project makes every day a little less ordinary by providing an inspirational quote from someone famous each day, customized to the user's preferences. It allows users to select specific categories and people that they would like to get quotes from on a daily basis, and provides a new quote each day sourced from [Brainy Quote](https://brainyquote.com).

## Mission Statement
* Inspiration Quotation seeks to inspire and motivate through the words of those who have already had success in life. With our Daily Quote, we hope to push you to become a better you every day, and we strive to personalize our message to your interests through our preferences page. At IQ, you won’t find anything superficial or generalized; every quote will be tailored to who you are to maximize your potential and improve your mindset each and every day.

## Requirements
* Node/npm
	* Download from [Node website](https://nodejs.org/en/) (LTS version is recommended).
* Python 
	* Operating systems such as MacOS and some Linux distributions have Python installed by default, but if you don't have it or want to update to the latest version visit the official [website](https://www.python.org/downloads/).
* Firebase
    * Visit the Firebase [site](https://firebase.google.com/) and go to console.
	* Hit the Add Project button and create a project (no need to add Google analytics).
	* Once the project is created, first go to authentication and hit Get Started. Hit email/password and enable it.
	* Then go to the Firestore Database Tab and hit Create Database, selecting Start in Test Mode (location settings do not matter).
	* Once the Firestore Database is created, hit Start Collection, and name it "users." The project will ask you to create a document, but the contents of the document do not matter.
	* Finally, go back to the Project Overview and click the Add App button, specifically the web one. Register the app (no need to select the "set up Firebase hosting" option). Once the app is registered, select the contents of the variable firebaseConfig and copy it to your clipboard. The contents should look like this:

```
{
	apiKey: "api-key",
	authDomain: "domain",
	projectId: "projectID",
	storageBucket: "storage",
	messagingSenderId: "ID",
	appId: "ID"
};
```
Make sure to select just the contents of the firebase Config variable, nothing else. Then navigate to the src folder and then to the components folder of the Vue app. In the components folder create a file named firebaseConfig.js. In the file type ```export default``` and paste the contents of the copied object. The file should look something like this:

```
export default  {
	apiKey: "api-key",
	authDomain: "domain",
	projectId: "projectID",
	storageBucket: "storage",
	messagingSenderId: "ID",
	appId: "ID"
};
```

## Project Setup
* After cloning and navigating to the repository, run ```npm install``` to install node modules.
* Move into the api folder using ```cd src/api```.
* Run ```pip install -r requirements.txt``` to install requirements such as Beautiful Soup, Flask and more.

## Run Project Locally
* To run the project, navigate to the root directory and type ```npm run serve``` to run the Vue app.
* Then run the Flask app by typing ```cd src/api``` and ```flask run```.
	* You should get the output: ```Running on http://127.0.0.1:5000``` if not, close any application runnining on port 5000 before doing ```flask run```
