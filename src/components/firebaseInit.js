import firebase from 'firebase/app';
import 'firebase/firestore';
import firebaseConfig from "./firebaseConfig";

const firebaseApp = firebase.initializeApp(firebaseConfig);
export default firebaseApp.firestore();