import React from "react";
import {withRouter} from 'react-router-dom'
import getPath from "../../pathResolver";
import Environment from "../environment/Environment";
import AddRow from "./AddRow";

class TableInfo extends React.Component {
    constructor(props) {
        super(props);
        this.showTitlesAndTypes = this.showTitlesAndTypes.bind(this);
        this.showRecords = this.showRecords.bind(this);
        this.deleteRow = this.deleteRow.bind(this);
        this.editRow = this.editRow.bind(this);
        this.state = {
            db: this.props.match.params.database,
            table: this.props.match.params.table,
            tableInfo: {},
            ok: false
        };
    }

    showTitlesAndTypes(columns, types) {
        if (!columns || !types) return null;

        let data = [];
        for (let i = 0; i < columns.length; i++) {
            data.push(<th>{columns[i]} ({types[i]})</th>);
        }
        return (<tr>{data}</tr>);
    }

    showRecords(records) {
        if (!records) return null;

        let data = [];
        for (let i = 0; i < records.length; i++) {
            data.push(
                <tr>
                    {records[i].map((val) => <td> {val} </td>)}
                    <td>
                        <button type={'button'} className={'link'} onClick={() => {
                            this.editRow(i)
                        }}> Edit
                        </button>
                    </td>
                    <td>
                        <button type={'button'} className={'link'} onClick={() => {
                            this.deleteRow(i)
                        }}> Delete
                        </button>
                    </td>
                </tr>
            );
        }
        return data;
    }

    editRow(index) {
        let data = prompt("Please enter column name and new value like 'column;value'", null);

        if (data == null || data === "") {
            return;
        }

        data = data.split(';');

        fetch(getPath('table', this.state.db, this.state.table), {
            method: 'PATCH',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({action: "update", index: index, column: data[0], value: data[1]})
        })
            .then(res => res.text())
            .then(res => {
                console.log(res);
                this.setState({ok: false});
            });
    }

    deleteRow(index) {
        fetch(getPath('table', this.state.db, this.state.table), {
            method: 'PATCH',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({action: "delete", index: index})
        })
            .then(res => res.text())
            .then(res => {
                console.log(res);
                this.setState({ok: false});
            });
    }

    render() {
        if (!this.state.ok) {
            fetch(getPath('table', this.state.db, this.state.table))
                .then(response => response.text())
                .then(json => {
                    this.setState({ok: true, tableInfo: JSON.parse(json)});
                });
        }

        return (
            <Environment>
                <table>
                    {this.showTitlesAndTypes(this.state.tableInfo.columns, this.state.tableInfo.types)}
                    {this.showRecords(this.state.tableInfo.records)}
                </table>
                <AddRow db={this.state.db} table={this.state.table} updateParent={
                    () => {
                        this.setState({ok: false});
                    }
                }/>
            </Environment>
        );
    }
}

export default withRouter(TableInfo);
