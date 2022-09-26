const initialIssues = [
    {
        id: 1,
        status: 'New',
        owner: 'Ravan',
        effort: 5,
        created: new Date('2018-08-15'),
        due: undefined,
        title: 'Error in console when clicking Add'
    },
    {
        id: 2,
        status: 'Assigned',
        owner: 'Eddie',
        effort: 14,
        created: new Date('2018-08-16'),
        due: new Date('2018-08-30'),
        title: 'Missing bottom border on panel'
    },
    {
        id: 3,
        status: 'New',
        owner: 'Elizabeth',
        effort: 9,
        created: new Date('2019-08-16'),
        due: new Date('2019-08-30'),
        title: 'Style missing bold component'
    },
    {
        id: 4,
        status: 'New',
        owner: 'Ravan',
        effort: 5,
        created: new Date('2018-08-15'),
        due: undefined,
        title: 'Error in console when clicking delete'
    },
    {
        id: 5,
        status: 'Assigned',
        owner: 'Ender',
        effort: 14,
        created: new Date('2010-08-16'),
        due: new Date('2011-08-30'),
        title: 'Typo on home page'
    },
    {
        id: 6,
        status: 'New',
        owner: 'Fender',
        effort: 9,
        created: new Date('2019-07-16'),
        due: new Date('2019-07-17'),
        title: 'Server got hit by bus'
    },
    {
        id: 7,
        status: 'New',
        owner: 'Ravie',
        effort: 5,
        created: new Date('2018-08-16'),
        due: undefined,
        title: 'Images won\'t load'
    },
    {
        id: 8,
        status: 'Assigned',
        owner: 'Eddington',
        effort: 14,
        created: new Date('2018-08-10'),
        due: new Date('2018-08-30'),
        title: 'Missing button on panel'
    },
    {
        id: 9,
        status: 'New',
        owner: 'Lizzie',
        effort: 96,
        created: new Date('1926-04-21'),
        due: new Date('2022-09-08'),
        title: 'Web page gone'
    },
    {
        id: 10,
        status: 'New',
        owner: 'Jimathon',
        effort: 9000,
        created: new Date('2019-07-16'),
        due: new Date('2019-08-30'),
        title: 'Style missing emphasized component'
    }
];



class IssueFilter extends React.Component {
    render() {
        return (
            <div>This is a placeholder for the Issue Filter</div>
        );
    }
}

function IssueRow(props){
    const issue = props.issue;

    return(
        <tr>
            <td>{issue.id}</td>
            <td>{issue.status}</td>
            <td>{issue.owner}</td>
            <td>{issue.created.toDateString()}</td>
            <td>{issue.effort}</td>
            <td>{issue.due ? issue.due.toDateString() : ''}</td>
            <td>{issue.title}</td>
        </tr>
    );
}

function IssueTable(props){
    const issueRows = props.issues.map(issue => <IssueRow issue={issue} />)

    return (
        <table className="bordered-table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Status</th>
                    <th>Owner</th>
                    <th>Created</th>
                    <th>Effort</th>
                    <th>Due Date </th>
                    <th>Title</th>
                </tr>
            </thead> 
            <tbody>
                {/* <IssueRow rowStyle={rowStyle} issue_id={1} issue_title="Error in console when clcking Add" />  */}
                {issueRows}
            </tbody>
        </table>
    );
}


class IssueAdd extends React.Component {
    constructor(){
        super();

        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(e) {
        e.preventDefault();
        const form = document.forms.issueAdd;
        const issue = {
            owner: form.owner.value,
            title: form.title.value,
            effort: form.effort.value,
            status: 'New'
        };

        this.props.createIssue(issue);
        form.owner.value = "";
        form.title.value = "";
        form.effort.value = "";
    }

    render() {
        return (
            <form name="issueAdd" onSubmit={this.handleSubmit}>
                <input type="text" name="owner" placeholder="Owner"/>
                <input type="text" name="title" placeholder="Title"/>
                <input type="text" name="effort" placeholder="Effort"/>
                <button>Add</button>
            </form>
        );
    }
}

class IssueList extends React.Component {
    constructor(){
        super();
        this.state = {issues: []};

        this.createIssue = this.createIssue.bind(this);

        // setTimeout(() => {
        //     this.createIssue(sampleIssue);
        // }, 2000);
    }
    
    createIssue(issue){
        issue.id = this.state.issues.length + 1;
        issue.created = new Date();
        const newIssueList = this.state.issues.slice();
        newIssueList.push(issue);
        this.setState({issues: newIssueList});
    }

    componentDidMount(){
    //    this.loadData();
    }

    loadData(){
        setTimeout(() => {
            this.setState({issues: initialIssues});
        }, 500);
    }

    

    render() {
        return (
            <React.Fragment>
                <h1>Issue Tracker</h1>
                <IssueFilter />
                <hr />
                <IssueTable issues={this.state.issues}/>
                <hr />
                <IssueAdd createIssue={this.createIssue}/>
            </React.Fragment>
        );
    }
}



const element = <IssueList />
    
ReactDOM.render(element, document.getElementById('contents'));