import React from "react";

class BookForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'name': '', 'author': props.authors[0]?.id}
        }

    handleChange(event) {
        this.setState(
        {[event.target.name]: event.target.value})
        }

    handleSubmit(event) {
        this.props.createBook(this.state.name, this.state.author)
        event.preventDefault()
    }

    render() {
        return(
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className = {"form-group"}>
                    <label form={"name"}>Name</label>
                    <input type="text" className="form-control"
                        name="name" value={this.state.name}
                        onChange={(event)=>this.handleChange(event) }/>
                </div>

                <div className = {"form-group"}>
                    <label form={"author"}>Author</label>

                    <select name="author" className="form-control" onChange={(event)=>this.handleChange(event)}>
                        {this.props.authors.map((item) => <option value={item.id}> {item.first_name}</option>)}
                    </select>

                </div>
                <input type="submit" className="btn btn-primary"
                        name="author" value="Save" />
            </form>
        )}
    }

export default BookForm