const e = React.createElement;

class CrawButton extends React.Component {
    constructor(props) {
        super(props);
        this.state = { crawed: false };
    }

    render() {
        if (this.state.crawed) {
            return "command executed";
        }

        return e(
            'button',
            { onClick: () => this.setState({ crawed: true }) },
            'Craw'
        );
    }
}

class UploadButton extends React.Component {
    constructor(props) {
        super(props);
        this.state = { uploaded: false };
    }

    render() {
        if (this.state.uploaded) {
            return "command executed";
        }

        return e(
            'button',
            { onClick: () => this.setState({ uploaded: true }) },
            'Upload'
        );
    }
}

class JSONButton extends React.Component {
    constructor(props) {
        super(props);
        this.state = { completed: false };
    }

    render() {
        if (this.state.completed) {
            return "command executed";
        }

        return e(
            'button',
            { onClick: () => this.setState({ completed: true }) },
            'ToJSON'
        );
    }
}

const crawContainer = document.querySelector('#craw_button');
const uploadContainer = document.querySelector('#upload_button');
const jsonContainer = document.querySelector('#ToJSON');
ReactDOM.render(e(CrawButton), crawContainer);
ReactDOM.render(e(UploadButton), uploadContainer);
ReactDOM.render(e(JSONButton), jsonContainer);

