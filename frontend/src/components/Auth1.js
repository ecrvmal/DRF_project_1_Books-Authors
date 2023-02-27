import React from 'react';


class LoginForm1 extends React.Component{
    constructor(props) {
        super(props);
        this.state = {'login':'','password':''}
    }


    render() {
        return (
            <form >
                <input type="text" name="login" placeholder="login" />
                <input type="password" name="password" placeholder="password" />
                <input type="submit" value="Login"/>
            </form>
        );
    }


}

export default LoginForm1
