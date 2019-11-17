import React from "react";

class Environment extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                    <div className={'container'}>
                        <a className={"navbar-brand mx-auto"}>
                            Система Керування Базами Даних
                        </a>
                    </div>
                </nav>
                <div className={'container'}>
                    {this.props.children}
                </div>
            </div>
        );
    }
}

export default Environment;