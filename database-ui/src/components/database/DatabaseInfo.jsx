import React from "react";
import {withRouter} from 'react-router-dom'
import getPath from "../../pathResolver";
import Environment from "../environment/Environment";
import CreateTable from "../table/CreateTable";

class DatabaseInfo extends React.Component {
    constructor(props) {
        super(props);
        this.deleteTable = this.deleteTable.bind(this);
        this.showTablesList = this.showTablesList.bind(this);
        this.state = {
            db: this.props.match.params.database,
            ok: false,
            tables: {}
        };
    }

    deleteTable(table) {
        if (window.confirm('Delete table?')) {
            fetch(getPath('table', this.state.db, table), {method: 'DELETE'})
                .then(res => res.text())
                .then(res => console.log(res))
                .then(res => this.setState({ok: false}));
        }
    }

    showTablesList(tables) {
        if (!tables) return null;
        return (
            tables.map((table) =>
                <li>
                    <a onClick={() => {
                        this.props.history.push('/databases/' + this.state.db + '/tables/' + table)
                    }}> {table} </a>
                    <button type={'button'} className={'link'} onClick={() => {
                        this.deleteTable(table)
                    }}> Delete
                    </button>
                </li>
            )
        );
    }

    render() {
        if (!this.state.ok) {
            fetch(getPath('database', this.state.db))
                .then(response => response.text())
                .then(json => {
                    this.setState({ok: true, tables: JSON.parse(json)});
                });
        }

        return (
            <Environment>
                <div className={'mt-4'}>
                    Список наявних таблиць в базі {this.state.db}:
                </div>
                <div className={'mt-2'}>
                    <ul>
                        {this.showTablesList(this.state.tables.tables)}
                    </ul>
                </div>
                <CreateTable db={this.state.db} updateParent={
                    () => {
                        this.setState({ok: false});
                    }
                }/>
            </Environment>
        );
    }
}

export default withRouter(DatabaseInfo);