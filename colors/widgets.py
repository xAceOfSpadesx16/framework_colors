from django import forms

class ColorChoiceWidget(forms.Select):
    template_name = 'color_select.html'
    option_template_name = 'color_select_option.html'

    def __init__(self, attrs=None, choices=None):
        super().__init__(attrs, choices)
        

    @staticmethod
    def _choice_has_empty_value(choice):
        value, _, _, _ = choice # modified to avoid ValueError too many to unpack
        return value is None or value == ""
    
    def optgroups(self, name, value, attrs=None):
        """Return a list of optgroups for this widget."""

        groups = []
        has_selected = False

        for index, (option_value, option_label, bg_css_class, text_css_class) in enumerate(self.choices):
            # modified to avoid ValueError too many to unpack
            if option_value is None:
                option_value = ""

            subgroup = []
            if isinstance(option_label, (list, tuple)):
                group_name = option_value
                subindex = 0
                choices = option_label
            else:
                group_name = None
                subindex = None
                choices = [(option_value, option_label)]
            groups.append((group_name, subgroup, index))

            for subvalue, sublabel in choices:
                selected = (not has_selected or self.allow_multiple_selected) and str(
                    subvalue
                ) in value
                has_selected |= selected
                subgroup.append(
                    self.create_option(
                        name,
                        subvalue,
                        sublabel,
                        selected,
                        index,
                        subindex=subindex,
                        attrs=attrs,
                        bg_css_class=bg_css_class,
                        text_css_class=text_css_class,
                    )
                )
                if subindex is not None:
                    subindex += 1
        return groups

    def create_option(
        self,
        name, 
        value, 
        label, 
        selected, 
        index, 
        subindex=None, 
        attrs=None, 
        bg_css_class='', #added
        text_css_class=''#added
    ): 
        index = str(index) if subindex is None else "%s_%s" % (index, subindex)
        option_attrs = (
            self.build_attrs(self.attrs, attrs) if self.option_inherits_attrs else {}
        )
        if selected:
            option_attrs.update(self.checked_attribute)
        if "id" in option_attrs:
            option_attrs["id"] = self.id_for_label(option_attrs["id"], index)
        return {
            "name": name,
            "value": value,
            "label": label,
            "text_css_class": text_css_class, #added
            "bg_css_class": bg_css_class, #added
            "selected": selected,
            "index": index,
            "attrs": option_attrs,
            "type": self.input_type,
            "template_name": self.option_template_name,
            "wrap_label": True,
        }
