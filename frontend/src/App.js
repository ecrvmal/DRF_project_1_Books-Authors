import React from 'react';
import ReactDOM from "react-dom";
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

import AuthorList from "./components/Author.js";
import BookList from "./components/Book.js";
import NotFound404 from "./components/NotFound404.js";
import BookListAuthors from "./components/BooksAuthor.js";

import LoginForm from "./components/Auth.js";
import LoginForm1 from "./components/Auth1.js";

import {HashRouter,Route,BrowserRouter,Link,Switch,Redirect} from "react-router-dom";

import Cookies from "universal-cookie"


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': [],
            'books':[],
            'token':'',
        }
    }

    load_data(){
        const headers = this.get_headers()
            axios.get('http://127.0.0.1:8000/api/authors/',{headers}).then(response => {
            this.setState(
                {
                    'authors': response.data
                }
            )}).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/books/',{headers}).then(response => {
            this.setState(
                {
                    'books': response.data
                }
            )}).catch(error => console.log(error))
    }

    set_token(token) {
//        # if work with localStorage:
//        # send to localStorage:
//        localStorage.setItem('token',token)
//        # get from localStorage:
//        let item = localStorage.getItem('token')

        const cookies = new Cookies()
        cookies.set('token',token)
//        установим состояние,
        this.setState({'token':token },()=>this.load_data())
   }

    get_token(username,password) {
//        console.log(username,password);
     axios.post('http://127.0.0.1:8000/api-token-auth/',
        {'username': username, password: password})
        .then(response => {
//        console.log(response.data['token'])
           this.set_token(response.data['token'])
            }).catch(error => alert('Login or password are incorrect'))

    }

    is_auth(){
    return !!this.state.token
    }

    get_headers(){
        let headers = {
            'Content-Type':'applications/json'
        }
        if(this.is_auth()) {
            headers['Authorization'] = `Token ${this.state.token}`  // special quots
        }
        return headers
    }

    logout(){
        this.set_token('')
    }

    get_token_from_cookies(){
        const cookies = new Cookies()
        const token = cookies.get('token')
//      установим состояние token, запускаем из текущего состояния load_data
        this.setState({'token':token },()=>this.load_data())
    }

    componentDidMount() {
        this.get_token_from_cookies();

    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                          {/* <Link to='/'> Authors</Link>} */}
                              <a href='/'> Authors </a>
                            </li>
                            <li>
                                {/* <Link to='/books'>Books</Link>} */}
                                <a href='/books'>Books</a>
                            </li>
                             <li>
                                 {this.is_auth()? <button onClick={()=> this.logout()}>Logout</button>:
                                     <a href='/login'>Login</a>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path="/" component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path="/books" component={() =>  <BookList books={this.state.books}/>}/>

                          {/*  for debug
                        <Route path='/author/:id'>
                            console.log('App.js')
                            console.log(f'{this.state.books}')
                            console.log(f'{this.state.authors}')
                        </Route>
                         */}

                        {/*   Alternative
                        <Route path='/author/:id'>
                            <BookListAuthors books={this.state.books} authors={this.state.authors}/>
                        </Route>
                         */}

                        <Route exact path="/author/:id" component={
                            () =>  <BookListAuthors books={this.state.books} authors={this.state.authors}/>}/>
                        {/*  /:id  отлавливается из BookAuthor.js через useParams  */}

                        <Route exact path="/login" component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>
                        {/* <Route exact path="/login" component={() => <LoginForm/>}/>  */}

                        <Redirect from="/book" to="/books" />
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;