<<<<<<< HEAD
from app import app

if __name__ == '__main__':
    app.run(debug=True)
=======
<<<<<<< HEAD
from app import app

if __name__ == '__main__':
    app.run(debug = True)
=======
from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__=='__main__':
    manager.run()
>>>>>>> 3c416bbb2737052b6fb177ba277bf5f7f6b20c75
>>>>>>> 2c38bc68549c550e73e7b665f4eee9da4fa87299
