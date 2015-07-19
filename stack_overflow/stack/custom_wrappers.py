from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

# import login_required user_passes_test
# these functions are made to be passed into user_passes_test


can_answer_func = lambda x: answer_score_check(x)
can_ask_func = lambda x:  question_score_check(x)

def answer_score_check(x):
    try:
        return Profile.objects.filter(pk=x.pk).filter(score__gte=125)
    except ObjectDoesNotExist:
        print('object doesnt exist')
        return redirect('stack:Login')
    except AttributeError:
        print('Attribute Error')
        return redirect('stack:Login')


def question_score_check(x):
    try:
       return Profile.objects.filter(pk=x.pk).filter(score__gte=25)
    except ObjectDoesNotExist:
        print('object doesnt exist')
        return redirect('stack:Login')
    except AttributeError:
        print('Attribute Error')
        return redirect('stack:Login')




'''
 from django.contrib.auth.decorators import login_required

@method_decorator(login_required(redirect_field_name='restaurant_app:login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    '''
'''

The above method_decorator setup can be copied and used to require login in
class based views.

        '''