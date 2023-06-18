Summary Sheet: What you need to know so far
1. Version Control Systems (VCS)

    Types: Centralised (CVCS) stores all file versions on a central server. Example: Subversion (SVN). Distributed (DVCS) ensures each user has a complete copy of the repository, allowing for more flexibility and offline work. Example: Git.
    Repository and Working Copy: A repository is a data structure that VCS creates to store metadata for a set of files and directories. A working copy is a single checkout of one version of the project.
    Git Commands:
        Branching creates a separate line of development.
        Pull fetches and merges changes from a remote repository to a local one.
        Push sends commits from a local repository to a remote one.
    Merging and Conflict Resolution: Merging integrates changes from different branches. Conflict resolution is the process of reconciling and merging conflicting changes, often assisted by merge tools such as KDiff3.

2. DevOps

    Overview and Role: DevOps is a set of practices that combines software development (Dev) and IT operations (Ops) for shorter development cycles and faster innovation.
    Lifecycle and Automation Tools: Web-Based DevOps Lifecycle Tools, such as GitHub, manage the lifecycle of an application from development to deployment, increasing collaboration, streamlining workflows, and automating tasks. Automation tools like Jenkins or GitHub actions automate repetitive tasks and improve efficiency and reliability.
    Integration with VCS: VCS can integrate with DevOps tools like issue trackers, CI/CD tools, code review tools. Example: GitHub Actions integrates with GitHub for CI/CD.

3. Workflow Processes

    Branch Workflows and Strategies: Organize work by feature, use clear and consistent branch/commit naming. Branch workflows include Pull-Request Workflow, GitFlow, and Feature Branch Workflow.
    Policies and Procedures: Key policies include Commit message guidelines, branch naming conventions, merge strategies. Documentation and understanding of procedures are crucial for maintaining a clean, understandable history and facilitate collaboration.

4. Commit Strategies

    Working vs Indiscriminate Commits: Working commits are changes that are well-tested and ready to be shared, while indiscriminate commits are changes that are not well-tested or documented. Indiscriminate commits can lead to confusion and reduce code quality.
    Version Control Best Practices: Include committing related changes, writing clear and detailed commit messages, maintaining clean, focused branches.
    DVCS Best Practices: Include committing frequently, leveraging local repository for complex merge/rebase operations, using pull requests for code review.

5. Impact of VCS

    On Collaboration, Code History, and Code Quality: VCS increase collaboration, maintain code history, improve code quality, facilitate testing and debugging, and speed up the development process.
    In Testing and Debugging: VCS facilitate tracking of changes, enable parallel testing of branches, support CI/CD practices.
    In CI/CD Practices: Version control is fundamental to Continuous Integration and Continuous Deployment by enabling multiple developers to work concurrently, integrating changes frequently, and delivering often.

6. Security and VCS

    Access Control and Change Tracking: VCS manage access control, maintain a record of changes, helps in identifying and reverting malicious changes.
    VCS and Agile Methodologies: VCS support Agile methodologies by facilitating incremental development, frequent integrations, and enabling fast responses to change.

