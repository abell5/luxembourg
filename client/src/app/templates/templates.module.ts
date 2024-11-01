// core
import { NgModule } from "@angular/core";

// modules
import { MaterialModule } from "../material/material.module";
import { SectionTemplateComponent } from "./section-template/section-template.component";


@NgModule({
    declarations: [SectionTemplateComponent],
    exports: [SectionTemplateComponent],
    imports: [MaterialModule],

})
export class TemplatesModule {}