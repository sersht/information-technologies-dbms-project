const CLIENT_URL = "http://127.0.0.1:5000";

const mapping = {
    'databasesList': () => {return CLIENT_URL + '/databases'},
    'database': (database) => {return CLIENT_URL + '/databases/' + database},
    'table': (database, table) => {return CLIENT_URL + '/databases/' + database + '/tables/' + table}
};

const getPath = (endpoint, ...args) => {
    return mapping[endpoint](...args);
};

export default getPath;