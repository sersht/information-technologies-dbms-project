import React from 'react'
import {withRouter} from 'react-router-dom'
import getPath from "../../pathResolver";

class CreateTable extends React.Component {

    constructor(props) {
        super(props);
        this.submit = this.submit.bind(this)
    }

    async submit() {
        let table = document.getElementById('name').value;
        let columns = (document.getElementById('columns').value).split(';');
        let types = (document.getElementById('types').value).split(';');

        await fetch(getPath('table', this.props.db, table), {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({types: types, columns: columns})
        })
            .then(res => res.text())
            .then(res => console.log(res));

        this.props.updateParent();
    }

    render() {
        return (
            <div className={'mt-5'}>
                <form>
                    <div className={'row'}>
                        <input type={'text'} placeholder={'name'} id={'name'}/>
                        <input type={'text'} placeholder={'columns'} id={'columns'}/>
                        <input type={'text'} placeholder={'types'} id={'types'}/>
                    </div>
                    <div className={'row mt-2'}>
                        <button type={'button'} onClick={() => this.submit()}>Create table</button>
                    </div>
                </form>
            </div>
        );
    }
}

// 'int', 'str', 'float', 'image', 'segment'

export default withRouter(CreateTable);
