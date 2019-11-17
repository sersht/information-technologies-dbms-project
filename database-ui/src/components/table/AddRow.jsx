import React from 'react'
import {withRouter} from 'react-router-dom'
import getPath from "../../pathResolver";

class AddRow extends React.Component {

    constructor(props) {
        super(props);
        this.submit = this.submit.bind(this)
    }

    async submit() {
        let values = (document.getElementById('values').value).split(';');

        await fetch(getPath('table', this.props.db, this.props.table), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({values: values})
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
                        <input type={'text'} placeholder={'values'} id={'values'}/>
                    </div>
                    <div className={'row mt-2'}>
                        <button type={'button'} onClick={() => this.submit()}>Add row</button>
                    </div>
                </form>
            </div>
        );
    }
}

// 'int', 'str', 'float', 'image', 'segment'

export default withRouter(AddRow);
