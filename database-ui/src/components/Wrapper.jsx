import React from "react"
import {Switch, Route, withRouter} from 'react-router-dom'
import DatabasesList from "./DatabasesList";
import DatabaseInfo from "./database/DatabaseInfo";
import TableInfo from "./table/TableInfo";

class Wrapper extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Switch>
                <Route exact path={'/'}>
                    <DatabasesList/>
                </Route>
                <Route exact path={'/databases/:database'}>
                    <DatabaseInfo/>
                </Route>
                <Route exact path={'/databases/:database/tables/:table'}>
                    <TableInfo/>
                </Route>
            </Switch>
        );
    }
}

export default withRouter(Wrapper);