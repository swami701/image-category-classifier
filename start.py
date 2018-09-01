import loadenv # noqa
import os
from app import app
import scripts
import logging
logging.basicConfig(
        level=int(os.getenv('LOG_LEVEL', logging.INFO)),
        format='%(asctime)-15s - %(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    if os.getenv('PROGRAM_NAME', 'app') == 'app':
        app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
    else:
        scripts.label_image.main()
