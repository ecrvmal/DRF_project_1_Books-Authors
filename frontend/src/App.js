import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
<<<<<<< HEAD
import UserList from './components/User.js'    // from User.js
=======
import AuthorList from './components/Author.js'    // from User.js
>>>>>>> e20202b72d6677c435063c007bfd3519e4b327e4

class App extends React.Component {


    constructor(props)  {           //    constructor props - set settings
        super(props)                // re-define parent settings
        this.state = {              // state (variables)  of App component
<<<<<<< HEAD
        'users':[]
=======
        'authors':[]
>>>>>>> e20202b72d6677c435063c007bfd3519e4b327e4
        }
    }


    componentDidMount(){                    // монтирует данные на нашу страницу

<<<<<<< HEAD
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
            this.setState(                                        // создаем состояние объекта
                {
                    'users': response.data
=======
        axios.get('http://127.0.0.1:8000/api/authors/').then(response => {
            this.setState(                                        // создаем состояние объекта
                {
                    'authors': response.data
>>>>>>> e20202b72d6677c435063c007bfd3519e4b327e4
                }
                )
            }
            ).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
//            Main App

<<<<<<< HEAD
             < UserList users={this.state.users} />
=======
             < AuthorList authors={this.state.authors} />
>>>>>>> e20202b72d6677c435063c007bfd3519e4b327e4
            </div>
        );
    }
}

export default App;
