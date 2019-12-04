import { Component, OnInit, Input } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Content } from '../../models';


@Component({
  selector: 'app-content-input',
  templateUrl: './content-input.component.html',
  styleUrls: ['./content-input.component.scss'],
})
export class ContentInputComponent implements OnInit {
  @Input() content: any;
  @Input() preview = false;
  contentForm: FormGroup;

  constructor(private formBuilder: FormBuilder) {
   }

  ngOnInit() {
    this.contentForm = this.formBuilder.group({
      'Title': [this.content.Title],
      'Body': [this.content.Body]
    })
    this.onChanged();
  }

  onChanged() {
    for (const field in this.contentForm.controls) { // 'field' is a string
      this.contentForm.get(field).valueChanges.subscribe(val => {
        this.content[field] = val
      })
    }
  }

  save() {
    //TODO: save to parents list
  }

  remove() {
    //TODO: remove from parents list
  }

}
