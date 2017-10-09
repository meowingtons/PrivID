Work in progess! Some functionality is not existent yet.

# PrivID
Privileged Access Management in Python.

PrivID is currently a password storage system written in Python. Clients interact through a set of REST APIs. Data is stored in MongoDB. An AngularJS based GUI is in the works.

Management of passwords/just-in-time access can be enabled through "clients" that call this REST API to make the necessary changes in downstream systems.

# Clients

PrivID utilizes "clients" to connect to downstream systems for password management and enable just-in-time access management. Clients can be written in any language that supports webhooks/websockets and REST APIs.

# Administrative Units

PrivID divides things into categories called "administrative units", that hopefully maps to the environment that it's integrating with.

Environments -> Applications -> Groups -> Accounts
  
 Each "administrative unit" can have a password policy, audit policy, set of ACLs, a friendly name and some other functionality (discussed in detail below) attached to it.
 
 If care is taken when onboarding systems into PrivID to fully map out the system into appropriate administrative units, management can be greatly simplified and reporting enhanced.
 
 ### Environments
 
 Environments are the highest level administrative unit in PrivID. An example config would be to create 3 environments, defined Dev/QA/Prod. Audit requirements are likely to differ between these, and environments provide an easy way to alter these without making many changes on lower level objects.
 
 ### Applications
 
 Applications in PrivID should map to applications in your environment, an example would be Active Directory. MongoDB enables a flexible schema, thus connection details for "clients" mentioned above can be stored on the application object in PrivID. Additionally, specific access rights can be given to the team that owns Active Directory, allowing them to view audit logs, request password changes, etc. for all accounts that are part of the Active Directory application.
 
 ### Groups
 
 Groups in PrivID generally map to the human teams your organization is divided into. For example, this makes it easy to grant access to Active Directories built-in "Administrator" account to anyone on your Active Directory team. A client may also store which downstream groups a set of account should be a member of in a given system. (Eg. Domain Admins, Enterprise Admins, etc.)
 
 ### Accounts
 
 Accounts in PrivID hav a 1:1 relationship with privileged accounts or secrets in a given system.
