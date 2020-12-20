'''
TTS
====

The :class:`TTS` provides provides access to public methods to
use text to speech of your device.

Simple Examples
---------------

To speak::

    >>> from plyer import tts
    >>> tts.speak(message=message)

Supported Platforms
-------------------
Android, iOS, Windows, OS X, Linux

'''

from os import name as os_name # to get os name

class TTS:
    '''
    TextToSpeech facade.
    '''

    def speak(self, message=''):
        '''Use text to speech capabilities to speak the message.

        :param message: What to speak
        :type message: str
        '''
        self._speak(message=message)

    # private

    def _speak(self, **kwargs):
        if os_name=='nt': # if windows
            import _win_tts
            _win_tts.speak(kwargs['message'])
        else:
            raise NotImplementedError()
