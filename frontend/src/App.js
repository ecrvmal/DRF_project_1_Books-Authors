import React from 'react';
import axios from 'axios'
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'    // from User.js

class App extends React.Component {


    constructor(props)  {           //    constructor props - set settings
        super(props)                // re-define parent settings
        this.state = {              // state (variables)  of App component
        'authors':[]
        }
    }


    componentDidMount(){                    // монтирует данные на нашу страницу

        axios.get('http://127.0.0.1:8000/api/authors/').then(response => {
            this.setState(                                        // создаем состояние объекта
                {
                    'authors': response.data
                }
                )
            }
            ).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
//            Main App

             < AuthorList authors={this.state.authors} />
            </div>
        );
    }
}

export default App;
