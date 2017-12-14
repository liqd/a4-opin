Deployment
===

The opin.me production installation and its staging and dev servers are deployed
on [platform.sh][platfrom_sh], which is a PaaS (Platform-as-a-Service)
hoster running ontop on [AWS][aws] and [Azure][azure].

Configuration
---

There are three important configuration files `.platfrom.app.yaml`,
`.platform/routes.yaml` and `.platfrom/services.yaml`, to understand thier content
consult the [platfrom.sh documentation][paltf_docs]

Platfrom.sh provides a git repository for updating the currently deployed source
code. If you push to a valid branch in that repository the platfrom.sh build script
will execute and deploy the application.

We usually have tree environments running:

| name               | platfrom.sh git branch | version            |
|--------------------|------------------------|--------------------|
| [production][oprod]| master                 | some release       |
| [stage][ostage]    | stage                  | same as prodcution |
| [dev][odev]        | dev                    | latest from travis |

From the production platform, one can reach stage and dev via appending `/@dev` or
`/@stage`. This is configured manually in the platfrom.sh enviroment setup.


Local preparations
---

Before running your first deployment you need to add your ssh key the your user account
on platfrom.sh and the users needs access to the environment to deploy.

If you have a second ssh key for platform.sh add the following to your `.ssh/config`.

```
Host *.platform.sh
	IdentityFile ~/.ssh/aws-eb
```

Add the platfrom.sh project as a git remote (replace the example with the correct git
url from platform.sh project configuration)

```
git add remote abcedefgh@git.de-1.platform.sh:abcedfghj.git
```

Workflow
---

To deploy just push a git branch into right platform.sh git branch (see table above).

```
git push platfrom master:dev
```

[aws]: https://aws.amazon.com
[azure]: https://azure.microsoft.com/
[oprod]: https://opin-platformsh-master.liqd.net/
[ostage]: https://opin-platformsh-master.liqd.net/@stage
[odev]: https://opin-platformsh-master.liqd.net/@dev
[platfrom_sh]: https://platform.sh
[platf_docs]: https://docs.platform.sh/
