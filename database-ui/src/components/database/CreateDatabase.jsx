import React from 'react'
import {withRouter} from 'react-router-dom'
import getPath from "../../pathResolver";

class CreateDatabase extends React.Component {

    constructor(props) {
        super(props);
        this.submit = this.submit.bind(this)
    }

    async submit() {
        let database = document.getElementById('dbName').value;
        await fetch(getPath('database', database), {method: 'POST'})
            .then(res => res.text())
            .then(res => console.log(res));
        this.props.updateParent();
    }

    render() {
        return (
            <div className={'mt-5'}>
                <form>
                    <div className={'row'}>
                        <input type={'text'} id={'dbName'}/>
                    </div>
                    <div className={'row mt-2'}>
                        <button type={'button'} onClick={() => this.submit()}>Create database</button>
                    </div>
                </form>
            </div>
        );
    }
}

export default withRouter(CreateDatabase);