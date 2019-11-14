import React from "react";
import {withRouter} from 'react-router-dom'
import getPath from "../../pathResolver";
import Environment from "../environment/Environment";
import CreateTable from "./CreateTable";

class TableInfo extends React.Component {
    constructor(props) {
        super(props);
        this.showTitlesAndTypes = this.showTitlesAndTypes.bind(this);
        this.showRecords = this.showRecords.bind(this);
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
                </tr>
            );
        }
        return data;
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
            </Environment>
        );
    }
}

export default withRouter(TableInfo);
