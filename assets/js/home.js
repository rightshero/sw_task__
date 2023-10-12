
class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

const requester = new XMLHttpRequest();

// constructing tree from a dictionary of parent id to list of children
function constructTree(parent) {
    if (!data[parent.val.id]) {
        return parent
    }

    if (data[parent.val.id].length !== 0) {
        parent.left = constructTree(new TreeNode({ "id": data[parent.val.id][0].id, "type": data[parent.val.id][0].type }))
        parent.right = constructTree(new TreeNode({ "id": data[parent.val.id][1].id, "type": data[parent.val.id][1].type }))
    }
    return parent
}

// root with -1 value to grab the root nodes from the dictionary
function getRootNode(server_data) {
    let root = new TreeNode({ id: "None", type: "dummy" })
    return constructTree(root, server_data)
}



function handleClick(checked, has_child, id) {
    if (checked && has_child) {
        console.log("checked")
    }
    else if (has_child) {
        console.log("unchecked")
    }
    else {
        updateData(BASE_URL, id)
        getData(BASE_URL)
    }
}

// pre-order traversal to render the tree of checkboxes
function preOrderRenderData(parent_container, root, level = -1, content = "") {

    if (root == null) {
        return
    }

    // helper function to build checkbox and return the container and the content e.g. (A-1-1-1) as a string
    const [container, Content] = buildCheckbox(root.val.id, root.val.type, level, content, parent_container)



    container.addEventListener('click', function (e) {
        let has_child = root.left !== null || root.right !== null
        let checked = e.target.checked
        let id = root.val.id
        handleClick(checked, has_child, id)
    })

    preOrderRenderData(container, root.left, level + 1, "SUB "+Content + "-1")
    preOrderRenderData(container, root.right, level + 1, "SUB "+Content + "-2")
}




// Only in the first load then it will be updated without reloading the page
const DATA_HOLDER = document.getElementById('data-holder');
let data = JSON.parse(DATA_HOLDER.textContent);
const root_div = document.getElementById('root')
let root = getRootNode(data)
const BASE_URL = "http://localhost:8000/"
const deleter = document.getElementById('deleter')
deleter.addEventListener('click', handleDelete)
preOrderRenderData(root_div, root)


// feed the data to the tree and render it
function getData(url) {
    requester.open('GET', url, false);
    requester.setRequestHeader('Content-Type', 'application/json');
    requester.onreadystatechange = function () {
        if (requester.readyState === 4 && requester.status === 200) {
            root_div.innerHTML = ""
            data = JSON.parse(requester.responseText);
            preOrderRenderData(root_div, getRootNode(data))
            return requester.responseText;
        }
    }
    requester.send();
}

// send post request to update the database (create new Two check boxes as sub categories)
function updateData(url, parent_id) {
    let data = new FormData();
    data.append('parent', parent_id);

    requester.open('POST', url, false);
    requester.send(data);
}

function deleteData(url) {
    requester.open('DELETE', url, false);
    requester.send();
}

function handleDelete() {
    deleteData(BASE_URL)
    getData(BASE_URL)
}


// helper function to build checkbox and return the container and the content e.g. (A-1-1-1) as a string
function buildCheckbox(id, type, level, content, parent_container) {
    let container = document.createElement('div')
    container.classList.add('sub-container')
    container.classList.add('form-check')
    container.id = id
    const input = document.createElement('input');

    input.classList.add('form-check-input');
    input.id = id;
    input.setAttribute('type', 'checkbox');
    input.setAttribute('value', id);
    const label = document.createElement('label')
    label.classList.add('form-check-label')
    label.setAttribute('for', id)

    parent_container.appendChild(container)

    if (id !== "None") {
        container.appendChild(input)
        container.appendChild(label)
    }

    if (level === 0) {
        input.textContent = type === "1" ? 'A' : 'B';
        content = type === "1" ? 'A' : 'B';
    }
    else if (level === 1) {
        input.textContent = type === "1" ? content[0] + '1' : content[0] + '2';
        content = type === "1" ? content[4] + '1' : content[4] + '2';
        content = 'SUB ' + content
    }

    label.textContent = content;

    return [container, content]

}




// just for testing
function printTree(root) {
    if (root == null) {
        return
    }
    console.log(root.val.id)
    printTree(root.left)
    printTree(root.right)
}
