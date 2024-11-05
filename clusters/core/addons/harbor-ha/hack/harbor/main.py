import asyncio
from harborapi import HarborAsyncClient
from harborapi.models import *
import argparse


async def add_retention_policy(client, project_id):
    print(f"Trying to add RetentionPolicy into project {project_id}")
    await client.create_retention_policy(
        RetentionPolicy(
            algorithm="or",
            rules=[
                RetentionRule(
                    action="retain",
                    template="nDaysSinceLastPush",
                    params={
                        "nDaysSinceLastPush": 1
                    },
                    tag_selectors=[
                        RetentionSelector(
                            kind="doublestar",
                            decoration="matches",
                            pattern="**",
                            extras='{"untagged":true}'
                        )
                    ],
                    scope_selectors={
                        "repository": [RetentionSelector(
                            kind="doublestar",
                            decoration="repoMatches",
                            pattern="**"
                        )]
                    }
                )
            ],
            trigger=RetentionRuleTrigger(
                kind="Schedule",
                settings={
                    'cron': '0 0 7 * * 1-5',
                }
            ),
            scope=RetentionPolicyScope(
                level="project",
                ref=project_id
            ),
        )
    )


async def update_retention_policy(client, retention_id, project_id):
    print(f"Trying to update RetentionPolicy of project {project_id}")
    await client.update_retention_policy(
        retention_id=retention_id,
        retention=RetentionPolicy(
            algorithm="or",
            rules=[
                RetentionRule(
                    action="retain",
                    template="nDaysSinceLastPush",
                    params={
                        "nDaysSinceLastPush": 1
                    },
                    tag_selectors=[
                        RetentionSelector(
                            kind="doublestar",
                            decoration="matches",
                            pattern="**",
                            extras='{"untagged":true}'
                        )
                    ],
                    scope_selectors={
                        "repository": [RetentionSelector(
                            kind="doublestar",
                            decoration="repoMatches",
                            pattern="**"
                        )]
                    }
                )
            ],
            trigger=RetentionRuleTrigger(
                kind="Schedule",
                settings={
                    'cron': '0 0 7 * * 1-5',
                }
            ),
            scope=RetentionPolicyScope(
                level="project",
                ref=project_id
            ),
        )
    )


async def process_policy_in_projects(client):
    projects = await client.get_projects()

    for project in projects:
        retention_id = await client.get_project_retention_id(project.name)

        if not retention_id:
            print(f"No retention policy found for project: id {project.project_id} name {project.name!r} ")
            await add_retention_policy(client, project.project_id)
        else:
            await update_retention_policy(client, retention_id, project.project_id)
            print(f"Retention policy found for project: id {project.project_id} name {project.name!r}")


async def create_harbor_project_if_not_exists(client, project_name):
    try:
        project = await client.get_project(project_name)
        print(f"Project '{project_name}' already exists with ID {project.project_id}")
    except Exception:
        print(f"Creating project '{project_name}'")
        await client.create_project(
            ProjectReq(
                project_name=project_name,
                public=False,
                metadata=ProjectMetadata(
                    auto_scan=True,
                ),
            )
        )
        print(f"Project '{project_name}' created")


async def process_create_project(client, project_names):
    for name in project_names:
        await create_harbor_project_if_not_exists(client, name)


def create_harbor_client(url, username, secret):
    client = HarborAsyncClient(url=url, username=username, secret=secret)
    return client


async def main():
    parser = argparse.ArgumentParser(description='Manage retention policies and projects in Harbor')
    parser.add_argument('--url', required=True, help='Harbor URL, e.g. "https://registry.com/api/v2.0"')
    parser.add_argument('--username', required=True, help='Harbor username, e.g. "admin"')
    parser.add_argument('--secret', required=True, help='Harbor secret, e.g. "123"')
    args = parser.parse_args()

    client = create_harbor_client(args.url, args.username, args.secret)

    # Set or update policy in all the projects of Harbor
    await process_policy_in_projects(client)

    project_names = [
        "example-project-1",
        "example-project-2",
    ]  # Add your project names here

    # Create projects in Harbor
    await process_create_project(client, project_names)


if __name__ == "__main__":
    asyncio.run(main())
