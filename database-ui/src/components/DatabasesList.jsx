import React from "react";
import getPath from "../pathResolver";
import Environment from "./environment/Environment";
import {withRouter} from 'react-router-dom'
import CreateDatabase from "./database/CreateDatabase";

class DatabasesList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {ok: false, databasesList: []};
        this.deleteDatabase = this.deleteDatabase.bind(this);
        this.showDatabasesList = this.showDatabasesList.bind(this);
    }

    deleteDatabase(database) {
        if (window.confirm('Delete database?')) {
            fetch(getPath('database', database), {method: 'DELETE'})
                .then(res => res.text())
                .then(res => console.log(res))
                .then(res => this.setState({ok: false}));
        }
    }

    showDatabasesList(databases) {
        return (
            databases.map((db) =>
                <li>
                    <a onClick={() => {
                        this.props.history.push('/databases/' + db)
                    }}> {db} </a>
                    <button type={'button'} className={'link'} onClick={() => {
                        this.deleteDatabase(db)
                    }}> Delete
                    </button>
                </li>
            )
        );
    }

    render() {
        if (!this.state.ok) {
            fetch(getPath('databasesList'))
                .then(response => response.text())
                .then(json => {
                    this.setState({ok: true, databasesList: JSON.parse(json)})
                });
        }

        return (
            <Environment>
                <div className={'mt-4'}>
                    Список наявних баз даних:
                </div>
                <div className={'mt-2'}>
                    <ul>
                        {this.showDatabasesList(this.state.databasesList)}
                    </ul>
                </div>
                <CreateDatabase updateParent={
                    () => {
                        this.setState({ok: false});
                    }
                }/>
            </Environment>
        );
    }
}

export default withRouter(DatabasesList);